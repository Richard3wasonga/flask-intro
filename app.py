from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello world!"

@app.route("/about")
def about():
    return "This is about us page"

@app.route("/<username>")
def username(username):
    return f'Hello {username}'

if __name__=='__main__':
    app.run(debug=True, port=4000)