from flask import Flask, request, jsonify, render_template



from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk




nltk.download('vader_lexicon')

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        inp = request.form.get("inp")
        sid = SentimentIntensityAnalyzer()
        score = sid.polarity_scores(inp)
        if score["neg"] != 0:
            return render_template("index2.html", message="Negative Feedback ☹️☹️")
        else:
            return render_template("index2.html", message="Positive Feed back 😁😁")
    return render_template("index2.html")


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
