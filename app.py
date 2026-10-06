from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def welcome():
    return "<center><h1>Welcome to the Flask App!</h1></center>"


@app.route("/greet/<name>")
def greet(name):
    return f"<center><h1>Hello, {name}!</h1></center>"

@app.route("/users", methods=["GET", "POST"])
def myProfile():
    data = None
    if request.method == 'POST':
        data = request.form
    return render_template('users.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)
