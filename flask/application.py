from flask import Flask, request, render_template

# from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


@app.route('/base')
def base():
    return render_template("base.html")


@app.route('/')
def index_page():
    return render_template("index.html")


@app.route('/application-form')
def application_form():
    return render_template("application-response.html")


@app.route('/application', methods=["POST"])
def application_submitted():
    fname = request.form.get("firstnameinput")
    lname = request.form.get("lastnameinput")
    salary = request.form.get("salaryrequirementinput")
    position = request.form.get("positionselection")
    return render_template("application-form.html", name=fname+" "+lname, salary=salary, position=position)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
