from openai import OpenAI
from dotenv import load_dotenv
import shutil
import subprocess
import os


def CreateVideo(question: str):
    global questionNum

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
        else:
            raise Exception(f"Run did not complete successfully. Status: {run.status}")


    def send_prompt(prompt: str, bot: str) -> str:
        add_message(prompt)
        messages = send_messages(bot)
        latest_message = messages.data[0]
        return latest_message.content[0].text.value

    latex_solution = send_prompt(question, LATEXBOT_ID)
    manimCode = send_prompt(latex_solution, MANIMBOT_ID)

    with open("Solution.py", "w") as f:
        txtManimCode = manimCode.replace('```', '').replace('python', '')
        f.write(txtManimCode)

    subprocess.run(['manim', '-ql', 'Solution.py', 'Solution'])
    shutil.copy2("media/videos/Solution/480p15/Solution.mp4", f"static/Solution{questionNum}.mp4")
    questionNum += 1

questionNum = 1
if __name__ == "__main__":
    CreateVideo("Differentiate x^x")