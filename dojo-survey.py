from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    name = request.form["name"]
    location = request.form["location"]
    language = request.form["language"]
    comment = request.form["comments"]
    return render_template("result.html",name=name,location=location,language=language,comment=comment)

@app.route("/danger")
def danger():
    print("user tried to visited /danger. redirecting to index page...")
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)