from flask import Blueprint, jsonify
from ..models.pizza import Pizza

pizza_bp = Blueprint('pizza_bp', __name__, url_prefix='/pizzas')

@pizza_bp.route('/', methods=['GET'])
def get_all_pizzas():
    pizzas = Pizza.query.all()
    response = [
        {"id": pizza.id, "name": pizza.name, "ingredients": pizza.ingredients}
        for pizza in pizzas
    ]
    return jsonify(response), 200
