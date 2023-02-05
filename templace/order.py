from flask import Blueprint, jsonify, request
from init_app import db
from models import Order

blueprint_order = Blueprint('blueprint', __name__)


@blueprint_order.route('/orders')
def get_orders():
    orders = Order.query.all()
    result = []
    for order in orders:
        result.append({
            'id': order.id,
            'name': order.name,
            'description': order.description,
            'state': order.state
        })
    return result


@blueprint_order.route('/orders/<int:id>')
def get_order(id):
    user = Order.query.get(id)
    return jsonify({
        'id': user.id,
        'name': user.name,
        'description': user.description,
        'start_date': user.start_date
    })


@blueprint_order.route('/offer')
def get_offers():
    offers = Order.query.all()
    result = []
    for offer in offers:
        result.append({
            'id': offer.id,
            'order_id': offer.order_id,
            'executor_id': offer.executor_id})
    return result


@blueprint_order.route('/orders', methods=['POST'])
def create_order():
    data = request.form
    new_order = Order(**data)
    db.session.add(new_order)
    db.session.commit()
    return jsonify({
        'id': new_order.id,
        'name': new_order.name,
        'price': new_order.price,
        'date': new_order.start_date})


@blueprint_order.route('/orders/<int:id>', methods=['PUT'])
def update_order(id):
    data = request.form
    result = Order.query.filter(Order.id == id).update(data)
    return result


@blueprint_order.route('/orders/<int:id>', methods=['DELETE'])
def delete_user(id):
    data = request.json
    result = Order.query.filter(Order.id == id).delete()
    db.session.commit()
    return f"Удалено успешно"

