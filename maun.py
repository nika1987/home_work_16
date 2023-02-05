from init_app import app
from templace.offer import blueprint_offer
from templace.order import blueprint_order
from templace.user import blueprint_user

app.register_blueprint(blueprint_order)
app.register_blueprint(blueprint_offer)
app.register_blueprint(blueprint_user)

app.run()
