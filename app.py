from flask import Flask, make_response
from models import db, User, Post
from flask_migrate import Migrate



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'

migrate = Migrate(app,db)
db.init_app(app)

@app.route("/")
def index():
    return "Hello world!"

@app.route("/about")
def about():
    return "This is about us page"

@app.route("/<username>")
def username(username):
    return f'Hello {username}'

@app.route('/posts')
def post():
    posts = Post.query.all()
    posts_list = [post.to_dict() for post in posts]
    return make_response(posts_list)
    

if __name__=='__main__':
    app.run(debug=True, port=4000)