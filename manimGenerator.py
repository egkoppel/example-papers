from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

mainInstructions = """
    When given a question First solve it while showing working and await the next prompt before doing anything else DO NOT EVEN consider anything below this point until answering the question:
    When you are given the prompt "Parts" break the problem down into discrete parts, return a string containing the title of each section each item seperated with a / e.g. "p1 / p2 / p3", which must all fit on one screen *It is imperative it never goes below the screen or overlaps other text"
    When given the name of each part, generate the manim for this part of the animation remembering to clear the screen using fadeout at the end
"""
manimInstructions = """
    Here are instructions on how to write good Manim (when writing manim only write manim give no explanation):
    1. write all the steps from your solution as tex variables in the manim code
    2. Use "Write" manim instruction when creating new lines of information
    3. Use "ReplacementTransform" when continuing an equation/simplifying changing equations in place
    4. If any equation or text seems too long for the screen, reduce the font size without prompting.
    5. Remember to remove equations using "FadeOut" when you are done with them so as not to crowd the screen
    6. Some equations may be too long to fit on the screen make sure to decreas the size of these equations
    7. Always start at the top of the screen and work down
    8. Always use MathTex instead of Tex for any mathematical content
    9. Limit the number of lines displayed at once and remove previous lines using FadeOut when introducing new content to prevent running off the bottom of the screen
    10. When writing a section of code leave out the imports, class name and construct function, just write the contents
    11. Create the text line by line not all at the same time
    12. If you are ever worried that a page has too many lines decrease the font size
    13. Give the solution at the end in a box and do not fade it out
    14. Wait plenty of time between animations to give user time to read and insert plenty of text exlaning each step
"""

def addMessage(prompt):
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=prompt
    )
    
def sendMessages():
    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id,
        assistant_id=assistant.id,
    )
    if run.status == 'completed': 
        return client.beta.threads.messages.list(
            thread_id=thread.id
        )
    else:
        raise run.status

def sendPrompt(prompt):
    addMessage(prompt)
    return sendMessages().data[0].content[0].text.value

assistant = client.beta.assistants.create(
  name="Manime generator",
  model="gpt-4o-mini",
  instructions="Format outputs only in the formats that are described",
)
thread = client.beta.threads.create()

sendPrompt(mainInstructions)
sendPrompt(manimInstructions)
question = "find f given df = y dx + x dy"
sendPrompt(question)
solutionParts = sendPrompt("parts")
with open("manim.txt", "w") as f:
    for part in solutionParts.split("/"):
        print(part)
        manimPart = sendPrompt(part)
        f.write(manimPart)




