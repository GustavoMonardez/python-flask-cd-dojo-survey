from flask import Flask, render_template, redirect, request, flash, session

app = Flask(__name__)
app.secret_key = "secret"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    name = request.form["name"]
    location = request.form["location"]
    language = request.form["language"]
    comment = request.form["comment"]
    print("comment:", comment)
     # session    
    session["name"] = name    
    session["location"] = location    
    session["language"] = language   
    session["comment"] = comment
    # validation
    if len(name) < 1 and len(comment) < 1:
        flash("Name cannot be empty!")
        flash("Comment cannot be empty!")
        return redirect("/")
    elif len(name) < 1:
        flash("Name cannot be empty!")
        return redirect("/")
    elif len(comment) < 1:
        flash("Comment cannot be empty!")
        return redirect("/")
    elif len(comment) > 120:
        print("session:",session["comment"])
        flash("Comment cannot have more than 120 characters!")
        return redirect("/")
   
    return render_template("result.html",name=name,location=location,language=language,comment=comment)

@app.route("/clear", methods=["POST"])
def clear():
    session.clear()
    return redirect("/")

@app.route("/danger")
def danger():
    print("user tried to visited /danger. redirecting to index page...")
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)