from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

client = OpenAI()


class PageSection(BaseModel):
    start_page: int
    end_page: int
    file_search_citation: str


class Question(BaseModel):
    question_number: str
    question_name: str
    topics: list[str]
    pages: list[PageSection]


class QuestionList(BaseModel):
    questions: list[Question]


assistant = client.beta.assistants.create(
    name="Che Fixer",
    instructions=f"You are a university tutor and have access to lecture notes through file_search. You will be given "
                 f"questions a student is failing miserably at. You will be given text of questions, and should list "
                 f"the relevant topics from the lecture notes as well as any relevant page numbers. You should output "
                 f"ONLY a json file according to the following schema. ```json\n"
                 f"{QuestionList.model_json_schema()}\n```",
    tools=[{"type": "file_search"}],
    model="gpt-4o-mini",
)

assistant = client.beta.assistants.update(
    assistant_id=assistant.id,
    tool_resources={"file_search": {"vector_store_ids": ["vs_67cc6233fb008191b683cbe63b091687"]}},
)

thread = client.beta.threads.create()

with open("thing8.txt", "r") as f:
    question_text = f.read()

message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content=f"Here is the list of questions:\n\n{question_text}",
)

run = client.beta.threads.runs.create_and_poll(
    thread_id=thread.id,
    assistant_id=assistant.id,
)

if run.status == 'completed':
    messages = client.beta.threads.messages.list(
        thread_id=thread.id
    )
    print(messages)
else:
    print(run.status)
    print(run.last_error)

    print(run)
