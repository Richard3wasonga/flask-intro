from flask import Flask, make_response, request
from models import db, User, Post
from flask_migrate import Migrate
from blueprint.user import user_bp
from blueprint.post import post_bp
from flask_restful import Api, Resource



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'

migrate = Migrate(app,db)
db.init_app(app)
api = Api(app)

#app.register_blueprint(user_bp)
#app.register_blueprint(post_bp)

#@app.route("/")
#def index():
#    return "Hello world!"

#@app.route("/about")
#def about():
    #return "This is about us page"

class PostEndpoint(Resource):
    def get(self):
        posts = [post.to_dict() for post in Post.query.all()]
        return make_response(posts, 200)

    def post(self):
        data = request.get_json()
        new_post = Post(post_title=data['post_title'], post_content=data['post_content'], user_id=data['user_id'])
        db.session.add(new_post)
        db.session.commit()

        return make_response(new_post.to_dict(), 201)

class PostEndpointById(Resource):
    def get(self, id):
        post = db.get_or_404(Post, id)
        return make_response(post.to_dict(), 200)
    
    def delete(self, id):
        post = db.get_or_404(Post, id)
        db.session.delete(post)
        db.session.commit()
        return make_response({'message': 'post deleted successfully'}, 200)

    def patch(self, id):
        post = db.get_or_404(Post, id)
        data = request.get_json()

        for key, value in data.items():
            setattr(post, key, value)
            
        db.session.commit()
        return make_response(post.to_dict(), 200)


api.add_resource(PostEndpoint, '/posts')
api.add_resource(PostEndpointById, '/posts/<int:id>')

if __name__=='__main__':
    app.run(debug=True, port=4000)