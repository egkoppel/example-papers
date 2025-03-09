from openai import OpenAI
from dotenv import load_dotenv
import shutil
import subprocess
import os
import random
import time


def CreateVideo(question: str, num: int):
    print(f"video for {num}")

    load_dotenv()
    client = OpenAI()
    LATEXBOT_ID = "asst_rqBGl40is1vvTGDITlkYcYZ6"
    MANIMBOT_ID = "asst_SQWSv3E3jCTnDFNAUx4cvndw"
    thread = client.beta.threads.create()


    def add_message(prompt: str):
        return client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=prompt
        )


    def send_messages(bot: str) -> str:
        run = client.beta.threads.runs.create_and_poll(
            thread_id=thread.id,
            assistant_id=bot,
        )
        if run.status == 'completed':
            return client.beta.threads.messages.list(thread_id=thread.id)
        elif run.last_error.code == 'rate_limit_exceeded':
            time.sleep(random.randint(1, 5))
            CreateVideo(question, num)
            return "FAIL"
        else:
            raise Exception(f"Run did not complete successfully. Status: {run.status}")


    def send_prompt(prompt: str, bot: str) -> str:
        add_message(prompt)
        messages = send_messages(bot)
        if messages == 'FAIL': return "FAIL"
        latest_message = messages.data[0]
        return latest_message.content[0].text.value

    latex_solution = send_prompt(question, LATEXBOT_ID)
    if latex_solution == "FAIL": return
    manimCode = send_prompt(latex_solution, MANIMBOT_ID)
    if manimCode == "FAIL": return

    with open(f"Solution{num}.py", "w") as f:
        txtManimCode = manimCode.replace('```', '').replace('python', '')
        f.write(txtManimCode)

    subprocess.run(['manim', '-ql', f'Solution{num}.py', f'Solution', "-o", f"Solution{num}.mp4"])

    shutil.copy2(f"media/videos/Solution{num}/480p15/Solution{num}.mp4", f"static/Solution{num}.mp4")

if __name__ == "__main__":
    CreateVideo("Differentiate x^x")