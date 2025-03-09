import werkzeug.datastructures
from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel
from pydantic_core import from_json
import time
import pymupdf
import base64

load_dotenv()

client = OpenAI()


class PageSection(BaseModel):
    model_config = dict(extra="forbid")
    start_page: int
    end_page: int
    file_search_citation: str


class Question(BaseModel):
    model_config = dict(extra="forbid")
    question_number: str
    question_content: str
    topics: list[str]
    pages: list[PageSection]


class QuestionList(BaseModel):
    model_config = dict(extra="forbid")
    questions: list[Question]


def parse_questions(pdf: werkzeug.datastructures.FileStorage):

    doc_gaslight = pymupdf.open("Exam questions/Question.pdf")
    page_gaslight = doc_gaslight.load_page(0)
    pix_gaslight = page_gaslight.get_pixmap(dpi=170)
    b_gaslight = pix_gaslight.tobytes(output='jpeg')
    base64_gaslight = base64.b64encode(b_gaslight).decode("utf-8")

    question_text = ""
    doc = pymupdf.open(stream=pdf.read(), filetype="pdf")
    for page in doc.pages():
        pix = page.get_pixmap(dpi=170)
        b = pix.tobytes(output='jpeg')
        base64_image = base64.b64encode(b).decode("utf-8")
        text = client.chat.completions.create(
            model="gpt-4o-mini",
            temperature=0.01,
            messages=[
                {
                    "role": "developer",
                    "content": "You are a helpful assistant who has been tasked with converting scans of old paper questions into modern digital LaTeX versions of the questions. When asked, please only provide the content of each page, and do not include any messages before or after the content. You will be given a series of images by the user and should return LaTeX text. Ensure ALL math is surrounded by $latex$."
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image_url",
                            "image_url": {"url": f"data:image/jpeg;base64,{base64_gaslight}", "detail": "high"},
                        },
                    ],
                },
                {
                    "role": "assistant",
                    "content": """13Z

(a) Solve the equation \\(\\frac{dy}{dx} = \\frac{y^2 + xy}{x^2}\\). [6]

(b) Show that \\((x + y)dx + x dy\\) is an exact differential, and use this to obtain the general solution of \\(\\frac{dy}{dx} + x + y = 0\\). [7]

(c) Solve the equation \\(\\frac{dy}{dx} + ky = a \\sin mx\\) subject to the boundary condition \\(y = 1\\) when \\(x = 0\\), where \\(k, m\\) and \\(a\\) are real, non-zero, constants. [7]"""
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image_url",
                            "image_url": {"url": f"data:image/jpeg;base64,{base64_image}", "detail": "high"},
                        },
                    ],
                }
            ],
        ).choices[0].message.content
        print(text)
        question_text += text
        question_text += "\n"

    doc.close()

    better = ""
    for thing in iter(question_text.splitlines()):
        if "```" not in thing:
            better += thing
            better += "\n"
    return better


def question_summary(better: str, notes: str):
    result = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "developer",
                "content": "You are a helpful assistant who is being asked by a lecturer to create a list of where students should look in the lecture notes when they get stuck on a question. When asked, please provide the question number and content copied from the question list, as well as a summary of the topics and the relevant page numbers in the notes. Ensure you use newlines."
            },
            {
                "role": "user",
                "content": f"""Here is the first set of questions:
{better}

And the content of the lecture notes - they are provided with sets of pages delimited by ======N====== where N is a page, or ======N-M====== where N-M is an INCLUSIVE range of pages:
{notes}"""
            },
        ],
        temperature=0.01,
        response_format=QuestionList
    ).choices[0].message.parsed

    print(repr(result))

    return result


if __name__ == "__main__":
    question_summary()
