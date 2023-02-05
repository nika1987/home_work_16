from pickle import GET

from flask import Blueprint, jsonify, request
from init_app import db
from models import Offer

blueprint_offer = Blueprint('blueprint', __name__)


@blueprint_offer.route('/offers')
def get_offer():
    offers = Offer.query.all()
    result = []
    for offer in offers:
        result.append({
            'id': offer.id,
            'order_id': offer.order_id,
            'executor_id': offer.executor_id
        })
    return jsonify(result)


@blueprint_offer.route('/offer/<int:id>')
def get_offer(id):
    offer = Offer.query.get(id)
    return jsonify({
        'id': offer.id,
        'order_id': offer.order_id,
        'executor_id': offer.executor_id
    })


@blueprint_offer.route('/offers', methods=['POST'])
def create_user():
    data = request.form
    new_offer = Offer(**data)
    db.session.add(new_offer)
    db.session.commit()
    return jsonify({
        'id': new_offer.id,
        'order_id': new_offer.order_id,
        'executor_id': new_offer.executor_id})


@blueprint_offer.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.json
    result = Offer.query.filter(Offer.id == id).update(data)
    db.session.commit()
    return f"Добавлено успешно"


@blueprint_offer.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    data = request.json
    result = Offer.query.filter(Offer.id == id).delete()
    db.session.commit()
    return f"Удалено успешно"
