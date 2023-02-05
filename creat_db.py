from maun import db
from utils import open_json
from maun import Order, User, Offer


def find_table(file_name, model):
    data = open_json(file_name)
    for item in data:
        obj = model(**item)
        db.session.add(obj)
    db.session.commit()


def create_table():
    db.create_all()
    find_table('data/offers.json', Offer)
    find_table('data/orders.json', Order)
    find_table('data/users.json', User)

#with app.app_context():
    #create_table()





