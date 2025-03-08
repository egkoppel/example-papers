from flask import Flask, render_template
import chatgpt

app = Flask(__name__)

@app.route("/")
def hello_world():
    questions = chatgpt.question_summary()
    return render_template("ui.html", questions=questions.questions)
