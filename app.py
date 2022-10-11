from flask import Flask, render_template, request
from utils import recognize_indo, recognize_english

app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html")


@app.route("/indonesian", methods=["GET", "POST"])
def indonesian():
    if request.method == "POST":
        text = request.form["text"]
        text = text.strip()
        if text:
            label, score = recognize_indo(text)
            return render_template("indonesia.html",
                                   text=text,
                                   label=label.capitalize(),
                                   score=round(score*100))
        else:
            return render_template("indonesia.html",
                                   alert="Please input some text to be recognized!")
    else:
        return render_template("indonesia.html")


@app.route("/english", methods=["GET", "POST"])
def english():
    if request.method == "POST":
        text = request.form["text"]
        text = text.strip()
        if text:
            label, score = recognize_english(text)
            return render_template("english.html",
                                   text=text,
                                   label=label.capitalize(),
                                   score=round(score*100))
        else:
            return render_template("english.html",
                                   alert="Please input some text to be recognized!")
    else:
        return render_template("english.html")


if __name__ == "__main__":
    app.run(debug=True)
