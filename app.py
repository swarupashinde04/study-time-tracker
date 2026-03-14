from flask import Flask, render_template, request

app = Flask(__name__)

days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

@app.route("/", methods=["GET","POST"])
def home():

    hours = []

    if request.method == "POST":

        for day in days:
            value = request.form.get(day)
            hours.append(float(value))

    return render_template("index.html", days=days, hours=hours)

app.run(debug=True)