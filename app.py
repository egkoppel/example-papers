from flask import Flask, render_template, request, Response, stream_with_context
import chatgpt
from manimGenerator import CreateVideo
import summarize

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello_world():
    return render_template("main_ui.html")


@app.route("/generate", methods=["POST"])
def generate():
    @stream_with_context
    def generate():
        single_question = chatgpt.Question(
            question_number="Upload an example paper",
            question_content="",
            topics=[],
            pages=[]  # Assuming no PageSection instances for this example
        )
        notes_summary = summarize.main("static/L24fullnotesp2.pdf")
        yield "###a###"
        question_list = chatgpt.QuestionList(questions=[single_question])
        if request.method == "POST":
            print(request.files)
            q = chatgpt.parse_questions(request.files["file"])
            yield "###b###"
            question_list = chatgpt.question_summary(q, notes_summary)
        yield render_template("ui.html", questions=question_list.questions)
    return Response(generate())

@app.route("/video", methods=["POST"])
def video():
    question = request.get_json()
    text = question["text"]
    num = question["num"]
    CreateVideo(text, int(num))
    return ""
