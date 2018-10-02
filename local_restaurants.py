from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

app = Flask(__name__)

# engine = create_engine(
#     'sqlite:///restaurantmenu.db')
# Base.metadata.bind = engine

# Fake Restaurants
restaurant = ()
restaurants = ()
items = ()
item = ()

restaurant = {'name': 'The CRUDdy Crab', 'id': '1'}

restaurants = [{'name': 'The CRUDdy Crab', 'id': '1'}, {
    'name': 'Blue Burgers', 'id': '2'}, {'name': 'Taco Hut', 'id': '3'}]


# Fake Menu Items
items = [{'name': 'Cheese Pizza', 'description': 'made with fresh cheese', 'price': '$5.99', 'course': 'Entree', 'id': '1'}, {'name': 'Chocolate Cake', 'description': 'made with Dutch Chocolate', 'price': '$3.99', 'course': 'Dessert', 'id': '2'}, {'name': 'Caesar Salad', 'description': 'with fresh organic vegetables',
                                                                                                                                                                                                                                                        'price': '$5.99', 'course': 'Entree', 'id': '3'}, {'name': 'Iced Tea', 'description': 'with lemon', 'price': '$.99', 'course': 'Beverage', 'id': '4'}, {'name': 'Spinach Dip', 'description': 'creamy dip with fresh spinach', 'price': '$1.99', 'course': 'Appetizer', 'id': '5'}]
item = {'name': 'Cheese Pizza', 'description': 'made with fresh cheese',
        'price': '$5.99', 'course': 'Entree'}


# Show All Restaurants
@app.route('/')
@app.route('/restaurants')
def showRestaurants():
    # return "This page will display all restaurants"
    restaurant = {'name': 'The CRUDdy Crab', 'id': '1'}

    restaurants = [{'name': 'The CRUDdy Crab', 'id': '1'}, {
        'name': 'Blue Burgers', 'id': '2'}, {'name': 'Taco Hut', 'id': '3'}]
    return render_template('restaurants.html', restaurants=restaurants)


# Add New Restaurant
@app.route('/restaurant/new', methods=['GET', 'POST'])
def newRestaurant():
    # return "This page allows the user to create a new restaurant"
    return render_template('newrestaurant.html')


# Edit Restaurant
@app.route('/restaurant/<int:restaurant_id>/edit', methods=['GET', 'POST'])
def editRestaurant():
    # return "This page allows the user to edit a restaurant"
    return render_template('editrestaurant.html', restaurant_id=restaurant.id)


# Delete Restaurant
@app.route('/restaurant/<int:restaurant_id>/delete', methods=['GET', 'POST'])
def deleteRestaurant():
    # return "This page allows the user to __ a restaurant"
    return render_template('deleterestaurant.html', restaurant_id=restaurant.id)


# Show Restaurant Menu
@app.route('/restaurant/<int:restaurant_id>')
@app.route('/restaurant/<int:restaurant_id>/menu')
def showMenu():
    # return "This page displays a restaurant's menu"
    return render_template('menu.html', restaurant_id=restaurant.id, items=items)


# Add New Menu Item
@app.route('/restaurant/<int:restaurant_id>/menu/new', methods=['GET', 'POST'])
def newMenuItem():
    # return "This page allows the user to add a new menu item"
    return render_template('newmenuitem.html', restaurant_id=restaurant_id)


# Edit Menu Item
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit', methods=['GET', 'POST'])
def editMenuItem():
    # return "This page allows the user to edit a menu item"
    return render_template('editmenuitem.html', restaurant_id=restaurant_id, menu_id=menu_id)


# Delete Menu Item
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete', methods=['GET', 'POST'])
def deleteMenuItem():
    # return "This page allows the user to delete a menu item"
    return render_template('deletemenuitem.html', restaurant_id=restaurant_id, menu_id=menu_id)


if __name__ == '__main__':
    # app.secret_key = ''
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
