import os
import logging
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.middleware.proxy_fix import ProxyFix

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create the Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "sweetiebell-dev-key")
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)  # needed for url_for to generate with https

# Product data
cakes = [
    {
        "id": "chocolate-cake",
        "name": "Chocolate Cake",
        "description": "Rich, moist chocolate cake with a velvety ganache.",
        "price": 35.99,
        "category": "cakes",
        "image": "https://pixabay.com/get/g6ff808090a64de3564820152030d404297f0cc9a54d3f4c458281af6caee96d0329a15aa2bc97e894bf0bf5a0e64da16adce4e39cfe807d1552ce77226d71447_1280.jpg"
    },
    {
        "id": "red-velvet",
        "name": "Red Velvet Cake",
        "description": "Classic red velvet with cream cheese frosting.",
        "price": 38.99,
        "category": "cakes",
        "image": "https://pixabay.com/get/g8c79243e2801f7e454c5b95891c75d861a85cfc97ac5fa86c4531ba33a8e942ed5650768f5410460e893b9a566a47107b03ed37a9ee938b0911e10f780c4ff4b_1280.jpg"
    },
    {
        "id": "carrot-cake",
        "name": "Carrot Cake",
        "description": "Spiced carrot cake with walnuts and cream cheese frosting.",
        "price": 32.99,
        "category": "cakes",
        "image": "https://pixabay.com/get/g99f68e510efffe600e8f66cd2d407d41292120b192e7d3f4f3f1bded104116ffde87d31ca082bc80cfa165fb8a085b7fdf1ffa7decc7643c3c5774e3ed7e4e1a_1280.jpg"
    },
    {
        "id": "cheesecake",
        "name": "Classic Cheesecake",
        "description": "Creamy New York style cheesecake with graham cracker crust.",
        "price": 40.99,
        "category": "cakes",
        "image": "https://pixabay.com/get/ge95be845c5d38b3d599aa1ff7928302ff2f8b733c95c1bac2f524dd7a3dd99bc4dbc405c32dc0497a82c785120fa79f772a3ec7dce129b27efa3498b7e435cfe_1280.jpg"
    }
]

muffins = [
    {
        "id": "blueberry-muffin",
        "name": "Blueberry Muffin",
        "description": "Tender muffin packed with juicy blueberries.",
        "price": 3.99,
        "category": "muffins",
        "image": "https://pixabay.com/get/ge66fdec480b886ebf5a6c6354eb7df33f14e28175febc8bf3d2b0a5d2fa92da08cb13a6c7780ed37531e38defd53ed0d74ca53a363e82c0f91d1695ed3f632e0_1280.jpg"
    },
    {
        "id": "chocolate-chip-muffin",
        "name": "Chocolate Chip Muffin",
        "description": "Soft muffin loaded with chocolate chips.",
        "price": 3.99,
        "category": "muffins",
        "image": "https://pixabay.com/get/gb676c7a3dfb642f243e0f6eaf54634d1b37d7f336cb294c867748caa793cb99c99cd505293a00485b8608e52b92ad50b1d172009a944646b703fe873ae292ed6_1280.jpg"
    },
    {
        "id": "banana-nut-muffin",
        "name": "Banana Nut Muffin",
        "description": "Moist banana muffin with crunchy walnuts.",
        "price": 3.99,
        "category": "muffins",
        "image": "https://pixabay.com/get/gbbe15dc5aa19dee530bf1f9f85ef03aef81f50c3b3d91d09bc49a6c9771842c4987c0e4e34913171db0a39da43c03071429f63b1ba3cab0d3a0fb3a20afc56a3_1280.jpg"
    },
    {
        "id": "pumpkin-muffin",
        "name": "Pumpkin Spice Muffin",
        "description": "Spiced pumpkin muffin with cinnamon streusel topping.",
        "price": 4.29,
        "category": "muffins",
        "image": "https://pixabay.com/get/g7f1344e2ff878cfbf47fc42c65e8c4db22e42e1a8007c275f061febf840214d2bbc730016f560212b8d5c09038ce51707d3865d53f91cebe77e322312069f5e0_1280.jpg"
    }
]

desserts = [
    {
        "id": "chocolate-eclair",
        "name": "Chocolate Éclair",
        "description": "Choux pastry filled with cream and topped with chocolate.",
        "price": 4.99,
        "category": "desserts",
        "image": "https://pixabay.com/get/gde3efb1437c7205f88d790ed9b6e3d4651202fc96efc4369dcc0befbea2b24a10b8fb4212dfd07ed057515b984d14481d909ef3991a62ae047ed38f259f1d896_1280.jpg"
    },
    {
        "id": "fruit-tart",
        "name": "Fresh Fruit Tart",
        "description": "Buttery tart shell filled with vanilla custard and topped with fresh fruits.",
        "price": 5.99,
        "category": "desserts",
        "image": "https://pixabay.com/get/gda5f344943f52015d56d940154a9a56f095d7b155cfce6075f1604dcaf39d423ec289003d4afdab9692c7a08c3a4f3a792c2fe9ff023d824a84dacee597c5b3c_1280.jpg"
    },
    {
        "id": "tiramisu",
        "name": "Tiramisu",
        "description": "Italian dessert with coffee-soaked ladyfingers and mascarpone.",
        "price": 5.99,
        "category": "desserts",
        "image": "https://pixabay.com/get/ga788b28ce086bbdae59b6ba1b6894383f902d746985d89e673fc847a360c054e402805730aaa3aa8d737ca7838f8faf6ab3e895b47208c73de95aed69b8deaa8_1280.jpg"
    },
    {
        "id": "macarons",
        "name": "Assorted Macarons",
        "description": "Delicate French almond meringue cookies with ganache filling.",
        "price": 2.50,
        "category": "desserts",
        "image": "https://pixabay.com/get/g6a639808389239d38e5ec7885937188c48cd058a90fbff08547ec09a783aaeaf6de71ae958e4809e38c3563550fb29212d7c89b322d51e083dbee12458d9c429_1280.jpg"
    }
]

# Combine all products
all_products = cakes + muffins + desserts

# Routes
@app.route('/')
def index():
    """Render the homepage"""
    featured_products = [
        cakes[0],
        muffins[0],
        desserts[0],
        cakes[1]
    ]
    return render_template('index.html', featured_products=featured_products)

@app.route('/products')
def products():
    """Render the products page"""
    return render_template('products.html', cakes=cakes, muffins=muffins, desserts=desserts)

@app.route('/products/<product_id>')
def product_detail(product_id):
    """Render the product detail page"""
    product = next((p for p in all_products if p['id'] == product_id), None)
    if not product:
        flash("Product not found", "error")
        return redirect(url_for('products'))
    return render_template('product_detail.html', product=product)

@app.route('/order', methods=['GET', 'POST'])
def order():
    """Handle the order form"""
    if request.method == 'POST':
        # In a real app, this would send an email or save to a database
        name = request.form.get('name')
        email = request.form.get('email')
        product = request.form.get('product')
        quantity = request.form.get('quantity')
        date = request.form.get('date')
        message = request.form.get('message')
        
        # Log the order details (in a real app, you'd save this to a database)
        app.logger.info(f"New order: {name}, {email}, {product}, {quantity}, {date}, {message}")
        
        flash("Thank you for your order! We'll contact you soon to confirm.", "success")
        return redirect(url_for('index'))
    
    return render_template('order.html', products=all_products)

@app.route('/about')
def about():
    """Render the about page"""
    return render_template('about.html')

@app.route('/contact')
def contact():
    """Render the contact page"""
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
