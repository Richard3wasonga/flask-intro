from flask import Blueprint, make_response, request
from models import db, Post

post_bp = Blueprint('post_bp', __name__)

@post_bp.route('/posts', methods=['POST', 'GET'])
def post():
    if request.method == 'GET':
        posts = Post.query.all()
        posts_list = [post.to_dict() for post in posts]
        return make_response(posts_list, 200)
    if request.method == 'POST':
        data = request.get_json()
        new_post = Post(post_title=data('post_title'), post_content=data('post_content'), user_id=data('user_id'))
        db.session.add(new_post)
        db.session.commit()

        return make_response(new_post.to_dict(), 201)
    
@post_bp.route('/posts/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def get_post_by_id(id):
    post = db.get_or_404(Post, id)
    if request.method == 'GET':
        return make_response(post.to_dict(), 200)
    if request.method == 'DELETE':
        db.session.delete(post)
        db.session.commit()
        return make_response({
            'message' : 'Post deleted succesfully'
        }, 204)