"""
1. Setting up the flask application
2. Displaying Product
3. Adding product to the cart
4. Viewing the cart
5. Placing an Order
6. Enhancements and Customization
"""

from flask import Flask, render_template, session, request, redirect, url_for
import re
from flask_login import UserMixin, LoginManager, login_user, logout_user, login_required, current_user
from math import ceil

app = Flask(__name__, static_folder="static")
app.secret_key = 'heroviredssh'

login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

# products_list = [
#     {
#         "id": 1,
#         "name": "Parle-G",
#         "category": "biscuit",
#         "price": "₹ 5",
#         "description": "Parle-G is a sweet glucose biscuit that is popular in India and other parts of the world. It is made with wheat flour, sugar, glucose, vegetable oil, and salt. Parle-G biscuits are known for their crispy texture, sweet taste, and affordable price.\nParle-G biscuits can be enjoyed on their own or with a cup of tea or coffee. They can also be used to make a variety of snacks and desserts, such as biscuit cake, biscuit pudding, and biscuit ice cream.",
#         "image_url": "/static/products_images/product_01.jpeg",
#     },
#     {
#         "id": 2,
#         "name": "Little Heart",
#         "category": "biscuit",
#         "price": "₹ 10",
#         "description": "Little Heart is a sweet heart-shaped biscuit that is popular in India. It is made with wheat flour, sugar, vegetable oil, and salt. Little Heart biscuits are known for their crispy texture, sugary coating, and fun shape.\nLittle Heart biscuits can be enjoyed on their own or with a cup of tea or coffee. They are also a popular snack for children.",
#         "image_url": "/static/products_images/product_02.jpeg",
#     },
# ]

products_list = {
    1: {
        "name": "Parle-G",
        "category": "Biscuit",
        "price": "₹ 5",
        "description": "Parle-G is a sweet glucose biscuit that is popular in India and other parts of the world. It is made with wheat flour, sugar, glucose, vegetable oil, and salt. Parle-G biscuits are known for their crispy texture, sweet taste, and affordable price.\nParle-G biscuits can be enjoyed on their own or with a cup of tea or coffee. They can also be used to make a variety of snacks and desserts, such as biscuit cake, biscuit pudding, and biscuit ice cream.",
        "image_url": "/static/products_images/product_01.jpeg",
    },
    2: {
        "name": "Little Heart",
        "category": "Cookies",
        "price": "₹ 10",
        "description": "Parle-G is a sweet glucose biscuit that is popular in India and other parts of the world. It is made with wheat flour, sugar, glucose, vegetable oil, and salt. Parle-G biscuits are known for their crispy texture, sweet taste, and affordable price.\nParle-G biscuits can be enjoyed on their own or with a cup of tea or coffee. They can also be used to make a variety of snacks and desserts, such as biscuit cake, biscuit pudding, and biscuit ice cream.",
        "image_url": "/static/products_images/product_02.jpeg",
    },
    3: {
        "name": "Unibic Choco Ripple Cookies",
        "category": "Cookies",
        "price": "₹ 20",
        "description": "Unibic Choco Ripple Cookies are a delicious and satisfying snack that is perfect for any time of day. Made with real chocolate chips and a crispy cookie base, these cookies are sure to please even the most discerning palate. Unibic Choco Ripple Cookies are made with the finest ingredients and are baked to perfection. They are also vegetarian and contain no eggs, making them a great option for people with dietary restrictions.",
        "image_url": "/static/products_images/product_03.jpg",
    },
    4: {
        "name": "Britannia Marie Gold Biscuits",
        "category": "Biscuit",
        "price": "₹ 10",
        "description": "Britannia Marie Gold Biscuits are a popular tea time snack in India and other parts of the world. They are made with wheat flour, sugar, vegetable oil, milk solids, and raising agents. Marie Gold biscuits are known for their crispy texture, light flavor, and affordable price. Britannia Marie Gold Biscuits are a good source of vitamins and minerals, including calcium, iron, and vitamin B12. They are also low in fat and cholesterol.",
        "image_url": "/static/products_images/product_04.jpg",
    }
}

cart = {}

users = {
    1: User(1, "herovired_001", "password1"),
    2: User(2, "herovired_002", "password2")
}

@login_manager.user_loader
def load_user(user_id):
    return users.get(int(user_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Validate the user input
        for user in users.values():
            if user.username == username and user.password == password:
                login_user(user)
                return redirect(url_for('protected'))
        return 'Invalid username or password'
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/protected')
@login_required
def protected():
    return 'Logged in as: ' + str(current_user.get_id())

@app.route("/")
def home():
    return "Welcome to my Flask application!"

@app.route('/products')
def products():
    page = request.args.get('page', 1, type=int)
    per_page = 2
    total_pages = ceil(len(products_list) / per_page)
    start = (page-1) * per_page
    end = start + per_page
    products_to_show = list(products_list.values())[start:end]
    return render_template('products.html', products=products_to_show, current_page=page, total_pages=total_pages)

@app.route('/filter')
def filter():
    category = request.args.get('category')
    filtered_products = [p for p in products_list.values() if p['category'] == category]
    return render_template('filtered_products.html', products=filtered_products)

@app.route('/cart/add/<int:product_id>', methods=['GET'])
def add_to_cart(product_id):
    product = next((product for product in products_list if product['id'] == product_id), None)
    
    if product:
        if 'cart' not in session:
            session['cart'] = []

        session['cart'].append(product)
        session.modified = True

        return f"Product added to cart successfully! Your cart now has {len(session['cart'])} items."
    else:
        return "Product not found!", 404

@app.route('/cart', methods=['GET'])
def view_cart():

    cart = session.get('cart', [])
    total_price = sum(float(re.sub(r"[^\d\-+\.]", "", product['price'])) for product in cart)
    
    return render_template('cart.html', cart=cart, total_price=total_price)

@app.route('/order', methods=['GET', 'POST'])
def place_order():
    cart = session.get('cart', [])

    if not cart:
        return "Your cart is empty, add products to the cart before placing an order."
    
    session['cart'] = []
    return "Your order has been placed successfully. Thank you for shopping with us."

@app.route('/search')
def search():
    query = request.args.get('query')
    filtered_products = [p for p in products_list.values() if query.lower() in p['name'].lower()]
    return render_template('search_results.html', products=filtered_products)




if __name__ == "__main__":
    app.run(debug=True)
