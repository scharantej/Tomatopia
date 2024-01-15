 
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

# Create a Flask app
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tomatoes.db'
db = SQLAlchemy(app)

# Define the Tomato model
class Tomato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    taste_profile = db.Column(db.String(80), nullable=False)
    nutritional_value = db.Column(db.Text, nullable=False)
    culinary_uses = db.Column(db.Text, nullable=False)

# Create the database tables
db.create_all()

# Define the main route
@app.route('/')
def index():
    # Query all tomatoes from the database
    tomatoes = Tomato.query.all()

    # Render the index page with the list of tomatoes
    return render_template('index.html', tomatoes=tomatoes)

# Define the product details route
@app.route('/product-details/<int:product_id>')
def product_details(product_id):
    # Query the tomato with the specified ID from the database
    tomato = Tomato.query.get_or_404(product_id)

    # Render the product details page with the tomato information
    return render_template('product-details.html', tomato=tomato)

# Define the add to cart route
@app.route('/add-to-cart', methods=['POST'])
def add_to_cart():
    # Get the product ID and quantity from the request form
    product_id = request.form.get('product_id')
    quantity = request.form.get('quantity')

    # Query the tomato with the specified ID from the database
    tomato = Tomato.query.get_or_404(product_id)

    # Add the tomato to the shopping cart
    cart.add(tomato, quantity)

    # Flash a success message
    flash('Tomato added to cart successfully!')

    # Redirect to the product details page
    return redirect(url_for('product_details', product_id=product_id))

# Define the checkout route
@app.route('/checkout')
def checkout():
    # Get the shopping cart items
    cart_items = cart.get_items()

    # Calculate the total price of the items in the cart
    total_price = cart.get_total_price()

    # Render the checkout page with the cart items and total price
    return render_template('checkout.html', cart_items=cart_items, total_price=total_price)

# Define the user registration route
@app.route('/user-registration')
def user_registration():
    # Render the user registration page
    return render_template('user-registration.html')

# Define the user account route
@app.route('/user-account')
def user_account():
    # Render the user account page
    return render_template('user-account.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
