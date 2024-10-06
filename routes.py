from flask import Blueprint, jsonify, request
from models import db, User, Post

bp = Blueprint('main', __name__)

@bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'id': user.id, 'username': user.username} for user in users])

@bp.route('/users', methods=['POST'])
def create_user():
    data = request.json
    new_user = User(username=data['username'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'id': new_user.id}), 201

@bp.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return jsonify([{
        'id': post.id,
        'title': post.title,
        'body': post.body,
        'author': post.author.username
    } for post in posts])

@bp.route('/posts', methods=['POST'])
def create_post():
    data = request.json
    new_post = Post(title=data['title'], body=data['body'], user_id=data['user_id'])
    db.session.add(new_post)
    db.session.commit()
    return jsonify({'id': new_post.id}), 201

@bp.route('/posts/<int:id>', methods=['GET'])
def get_post(id):
    post = Post.query.get_or_404(id)
    return jsonify({
        'id': post.id,
        'title': post.title,
        'body': post.body,
        'author': post.author.username
    })
