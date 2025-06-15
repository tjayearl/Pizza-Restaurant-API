# Pizza Restaurant API

A RESTful Flask API for managing restaurants, pizzas, and their relationships.

## Features

- View all restaurants and their pizzas
- Add new restaurant-pizza relationships
- Delete a restaurant
- View all pizzas

## Technologies Used

- Python + Flask
- SQLAlchemy + Flask-Migrate
- SQLite

## Setup Instructions

```bash
git clone https://github.com/tjayearl/Pizza-Restaurant-API.git
cd Pizza-Restaurant-API
pip install -r requirements.txt
export FLASK_APP=server/app.py
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
flask run
