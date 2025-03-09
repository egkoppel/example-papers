from flask import Flask, render_template, request
import chatgpt
from manimGenerator import CreateVideo
import summarize

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def hello_world():
    single_question = chatgpt.Question(
        question_number="Upload an example paper",
        question_content="",
        topics=[],
        pages=[]  # Assuming no PageSection instances for this example
    )
    notes_summary = summarize.main("static/L24fullnotesp2.pdf")
    question_list = chatgpt.QuestionList(questions=[single_question])
    if request.method == "POST":
        print(request.files)
        question_list = chatgpt.question_summary(request.files["file"], notes_summary)
        CreateVideo(question_list.questions[0])
    return render_template("ui.html", questions=question_list.questions)
