from openai import OpenAI
from dotenv import load_dotenv
import subprocess
import os


load_dotenv()
client = OpenAI()
LATEXBOT_ID = "asst_rqBGl40is1vvTGDITlkYcYZ6"
MANIMBOT_ID = "asst_SQWSv3E3jCTnDFNAUx4cvndw"

QUESTION = """
Van der Waals’s equation (
p + a
V 2
)
(V − b) = RT
is an early (and in many ways a remarkably successful) attempt to represent the
relation between the pressure p, volume V and temperature T of a real gas. (R, a
and b are constants for a given mass of the gas.) Find expressions for (∂p/∂V )T ,
(∂V /∂T )p and (∂T /∂p)V , and verify that their product is −1
"""

# Create an assistant and threadÛ
# assistant = client.beta.assistants.create(
#     name="Larry",
#     model="gpt-4o",
#     instructions=MAIN_INSTRUCTIONS,
# )
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

latex_solution = send_prompt(QUESTION, LATEXBOT_ID)
print(latex_solution)
manimCode = send_prompt(latex_solution, MANIMBOT_ID)

with open("Solution.py", "w") as f:
    txtManimCode = manimCode.replace('```', '').replace('python', '')
    f.write(txtManimCode)

# """
# from manim import *

# class Solution(Scene):
#     def construct(self):
# """
#     )
#     for part in solution_parts.split("/"):
#         print("Processing part:", part)
#         manimPart = send_prompt(part)
#         manimPart = manimPart.replace('```', '').replace('python', '').replace('from manim import *', '')
#         for line in manimPart.split("\n"):
#             f.write("        " + line + "\n")

subprocess.run(['manim', '-ql', 'Solution.py', 'Solution'])