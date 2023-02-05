from flask import Blueprint, jsonify, request
from init_app import db
from models import User

blueprint_user = Blueprint('blueprint', __name__)


@blueprint_user.route('/users')
def get_users():
    users = User.query.all()
    result = []
    for user in users:
        result.append({
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
        })

    return jsonify(result)


@blueprint_user.route('/users/<int:id>')
def get_user(id):
    user = User.query.get(id)
    return jsonify({
        'id': user.id,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email
    })


@blueprint_user.route('/users', methods=['POST'])
def create_user():
    data = request.form
    new_user = User(**data)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({
        'id': new_user.id,
        'last_name': new_user.last_name,
        'first_name': new_user.first_name,
        'age': new_user.age,
        'email': new_user.email
    })


@blueprint_user.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.json
    result = User.query.filter(User.id == id).update(data)
    db.session.commit()
    return f"Добавлено успешно"


@blueprint_user.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    data = request.json
    result = User.query.filter(User.id == id).delete()
    db.session.commit()
    return f"Удалено успешно"
