from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

app = Flask(__name__)

engine = create_engine(
    'sqlite:///restaurantmenu.db')
Base.metadata.bind = engine


# Show All Restaurants
@app.route('/')
@app.route('/restaurants')
def showRestaurants():
    return "This page will display all restaurants"


# Add New Restaurant
@app.route('/restaurant/new', methods=['GET', 'POST'])
def newRestaurant():
    return "This page allows the user to create a new restaurant"


# Edit Restaurant
@app.route('/restaurant/<int:restaurant_id>/edit', methods=['GET', 'POST'])
def editRestaurant():
    return "This page allows the user to edit a restaurant"


# Delete Restaurant
@app.route('/restaurant/<int:restaurant_id>/delete', methods=['GET', 'POST'])
def deleteRestaurant():
    return "This page allows the user to __ a restaurant"


# Show Restaurant Menu
@app.route('/restaurant/<int:restaurant_id>')
@app.route('/restaurant/<int:restaurant_id>/menu')
def showMenu():
    return "This page displays a restaurant's menu"


# Add New Menu Item
@app.route('/restaurant/<int:restaurant_id>/menu/new', methods=['GET', 'POST'])
def newMenuItem():
    return "This page allows the user to add a new menu item"


# Edit Menu Item
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit', methods=['GET', 'POST'])
def editMenuItem():
    return "This page allows the user to edit a menu item"


# Delete Menu Item
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete', methods=['GET', 'POST'])
def deleteMenuItem():
    return "This page allows the user to delete a menu item"


if __name__ == '__main__':
    # app.secret_key = ''
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
