from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

app = Flask(__name__)

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine


# Show All Restaurants
@app.route('/')
@app.route('/restaurants')
def showRestaurants():
    # return "This page will display all restaurants"
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    restaurants = session.query(
        Restaurant).all()
    return render_template('restaurants.html', restaurants=restaurants)


# Add New Restaurant
@app.route('/restaurant/new', methods=['GET', 'POST'])
def newRestaurant():
    # return "This page allows the user to create a new restaurant"
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    if request.method == 'POST':
        newRestaurant = Restaurant(
            name=request.form['name'])
        session.add(newRestaurant)
        session.commit()
        flash("New Restaurant Created!")
        return redirect(url_for('showRestaurants'))
    else:
        return render_template('newrestaurant.html')


# Edit Restaurant
@app.route('/restaurant/<int:restaurant_id>/edit', methods=['GET', 'POST'])
def editRestaurant(restaurant_id):
    # return "This page allows the user to edit a restaurant"
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    editedRestaurant = session.query(
        Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedRestaurant.name = request.form['name']
        session.add(editedRestaurant)
        session.commit()
        flash("Restaurant Successfully Edited!")
        return redirect(url_for('showRestaurants'))
    else:
        return render_template('editrestaurant.html', restaurant_id=restaurant_id, restaurant=editedRestaurant)


# Delete Restaurant
@app.route('/restaurant/<int:restaurant_id>/delete', methods=['GET', 'POST'])
def deleteRestaurant(restaurant_id):
    # return "This page allows the user to __ a restaurant"
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    deletedRestaurant = session.query(
        Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        session.delete(deletedRestaurant)
        session.commit()
        flash("Restaurant Successfully Deleted!")
        return redirect(url_for('showRestaurants'))
    else:
        return render_template('deleteRestaurant.html', restaurant=deletedRestaurant)


# Show Restaurant Menu
@app.route('/restaurant/<int:restaurant_id>')
@app.route('/restaurant/<int:restaurant_id>/menu')
def showMenu(restaurant_id):
    # return "This page displays a restaurant's menu"
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    restaurant = session.query(
        Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(
        restaurant_id=restaurant.id)
    return render_template('menu.html', restaurant=restaurant, items=items)


# Add New Menu Item
@app.route('/restaurant/<int:restaurant_id>/menu/new', methods=['GET', 'POST'])
def newMenuItem(restaurant_id):
    # return "This page allows the user to add a new menu item"
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    if request.method == 'POST':
        newItem = MenuItem(
            name=request.form['name'], description=request.form['description'],
            price=request.form['price'], restaurant_id=restaurant_id)
        session.add(newItem)
        session.commit()
        flash("Menu Item Created!")
        return redirect(url_for('showMenu', restaurant_id=restaurant_id))
    else:
        return render_template('newmenuitem.html', restaurant_id=restaurant_id)


# Edit Menu Item
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit', methods=['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
    # return "This page allows the user to edit a menu item"
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    editedItem = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
            editedItem.description = request.form['description']
            editedItem.price = request.form['price']
        session.add(editedItem)
        session.commit()
        flash("Menu Item Successfully Edited!")
        return redirect(url_for('showMenu', restaurant_id=restaurant_id))
    else:
        return render_template('editmenuitem.html', restaurant_id=restaurant_id, menu_id=menu_id, item=editedItem)


# Delete Menu Item
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete', methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
    # return "This page allows the user to delete a menu item"
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    deletedItem = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        session.delete(deletedItem)
        session.commit()
        flash("Menu Item Successfully Deleted!")
        return redirect(url_for('showMenu', restaurant_id=restaurant_id))
    else:
        return render_template('deletemenuitem.html', restaurant_id=restaurant_id, menu_id=menu_id, item=deletedItem)


# JSON API Endpoints Below******************************************************
# Show All Restaurants - JSON
@app.route('/restaurants/JSON')
def showRestaurantsJSON():
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    restaurants = session.query(Restaurant).all()
    return jsonify(Restaurants=[r.serialize for r in restaurants])


# Show Restaurant Menu - JSON
@app.route('/restaurant/<int:restaurant_id>/menu/JSON')
def showRestaurantMenuJSON(restaurant_id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    restaurant = session.query(
        Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(
        restaurant_id=restaurant.id)
    return jsonify(MenuItems=[i.serialize for i in items])


# Show Menu Item - JSON
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/JSON')
def showMenuItemJSON(restaurant_id, menu_id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    item = session.query(MenuItem).filter_by(id=menu_id).one()
    return jsonify(MenuItem=item.serialize)


# ******************************************************************************
if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
