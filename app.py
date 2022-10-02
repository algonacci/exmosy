from flask import Flask, render_template, request
from utils import recognize

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["text"]
        if text:
            label, score = recognize(text)
            return render_template("index.html",
                                    text=text,
                                    label=label.capitalize(),
                                    score=round(score*100))
        else:
            return render_template("index.html",
            alert="Please input some text to be recognized!")    
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)