import sys

from flask import Flask, request, render_template

# Create flask app
app = Flask(__name__)


@app.route("/")
def Home():
    return render_template("index.html")


@app.route("/crop_summary", methods=["POST"])
def crop_summary():
    value = request.form.get('crop-list')
    return value



if __name__ == "__main__":
    app.run(debug=True)
