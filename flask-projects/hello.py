from flask import Flask, render_template

app = Flask(__name__)

""" 
@app.route('/bye')
def bye():
    return "Bye" 

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello {name}. You will make it. Keep trying, your wealth will be {number} billions dollars"

"""


@app.route('/')
def hello_world():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)