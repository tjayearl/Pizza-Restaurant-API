from ..app import db

class RestaurantPizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)

    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurant.id"), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey("pizza.id"), nullable=False)

    @staticmethod
    def validate_price(price):
        return 1 <= price <= 30
