# Local Restaurants

## Overview
This is a web application that lists a number of local restaurants and contains pages with their corresponding menus. The user can also add, edit, and delete both restaurants and menu items.


## Running the application
This web application is run on the localhost (port 5000) using python and is developed using the flask framework. You will need to install the flask library using the ```pip install flask``` command. Once installed the application can be run from the current directory by running the ```python local_restaurants.py``` command.


## _Web Pages_
This web app contains the following pages:

1. _All restaurants_ (```/restaurants```)
2. _Add New Restaurant_ (```/restaurant/new```)
3. _Edit Restaurant_ (```/restaurant/<int:restaurant_id>/edit```)
4. _Delete Restaurant_ (```/restaurant/<int:restaurant_id>/delete```)
5. _Restaurant Menu_ (```/restaurant/<int:restaurant_id>/menu```)
6. _Add New Menu Item_ (```/restaurant/<int:restaurant_id>/menu/new```)
7. _Edit Menu Item_ (```/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit```)
8. _Delete Menu Item_ (```/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete```)
