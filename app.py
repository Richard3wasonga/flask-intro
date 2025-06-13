from flask import Flask, make_response, request
from models import db
from flask_migrate import Migrate
from blueprint.user import user_bp
from blueprint.post import post_bp



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'

migrate = Migrate(app,db)
db.init_app(app)

app.register_blueprint(user_bp)
app.register_blueprint(post_bp)

@app.route("/")
def index():
    return "Hello world!"

@app.route("/about")
def about():
    return "This is about us page"

if __name__=='__main__':
    app.run(debug=True, port=4000)