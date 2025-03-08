from flask import Flask, render_template, request
import chatgpt

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def hello_world():
    print(request.files)
    single_question = chatgpt.Question(
        question_number="1",
        question_content="What is the capital of France?",
        topics=["Geography", "European Capitals"],
        pages=[chatgpt.PageSection(start_page=57,end_page=58, file_search_citation="L24fullnotesp2.pdf")]  # Assuming no PageSection instances for this example
    )
    #questions = chatgpt.question_summary()
    question_list = chatgpt.QuestionList(questions=[single_question])
    return render_template("ui.html", questions=question_list.questions)

