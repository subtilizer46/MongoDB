from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/infy'  # Update with your MongoDB URI
mongo = PyMongo(app)

# Create a collection for restaurants if it doesn't exist
if 'restaurants' not in mongo.db.list_collection_names():
    mongo.db.create_collection('restaurants')
    mongo.db.restaurants.insert_many([
        {
            'name': 'Restaurant 1',
            'cuisine': 'Italian',
            'location': 'City 1',
        },
        {
            'name': 'Restaurant 2',
            'cuisine': 'Mexican',
            'location': 'City 2',
        },
        # Add more restaurants as needed
    ])

# Create a collection for bookings if it doesn't exist
if 'bookings' not in mongo.db.list_collection_names():
    mongo.db.create_collection('bookings')

# Define routes and views
@app.route('/')
def index():
    restaurants = mongo.db.restaurants.find()
    return render_template('index.html', restaurants=restaurants)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/book/<restaurant_id>', methods=['GET', 'POST'])
def book(restaurant_id):
    if request.method == 'POST':
        name = request.form.get('name')
        date = request.form.get('date')
        booking = {
            'restaurant_id': restaurant_id,
            'name': name,
            'date': date
        }
        mongo.db.bookings.insert_one(booking)
        return redirect(url_for('index'))
    else:
        return render_template('booking.html', restaurant_id=restaurant_id)

if __name__ == '__main__':
    app.run(debug=True)
