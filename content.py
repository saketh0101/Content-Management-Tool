rom flask import Flask, render_template

app = Flask(_name_)

@app.route("/")
def content():
    return render_template("content.html")

if _name_ == "_main_":
    app.run()