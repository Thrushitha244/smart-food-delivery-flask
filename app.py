from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

cart = []

# 🍽️ FULL MENU (ALL YOUR FOOD ITEMS RESTORED)

restaurants = {

    "Andhra Meals": [
        {"name": "Veg Meals", "price": 120},
        {"name": "Mini Meals", "price": 100},
        {"name": "Chicken Curry Rice", "price": 180},
        {"name": "Mutton Curry Rice", "price": 220},
        {"name": "Fish Curry Rice", "price": 200},
        {"name": "Curd Rice", "price": 90},
        {"name": "Lemon Rice", "price": 100},
        {"name": "Pulihora", "price": 90},
        {"name": "Tomato Rice", "price": 95},
        {"name": "Jeera Rice", "price": 110},
        {"name": "Ghee Rice", "price": 130}
    ],

    "Biryani House": [
        {"name": "Chicken Biryani", "price": 180},
        {"name": "Mutton Biryani", "price": 250},
        {"name": "Egg Biryani", "price": 150},
        {"name": "Veg Biryani", "price": 130},
        {"name": "Paneer Biryani", "price": 170},
        {"name": "Fish Biryani", "price": 210},
        {"name": "Prawn Biryani", "price": 260},
        {"name": "Hyderabadi Biryani", "price": 200},
        {"name": "Dum Biryani", "price": 190}
    ],

    "Fast Food & Chinese": [
        {"name": "Veg Noodles", "price": 140},
        {"name": "Chicken Noodles", "price": 170},
        {"name": "Egg Noodles", "price": 150},
        {"name": "Veg Fried Rice", "price": 130},
        {"name": "Chicken Fried Rice", "price": 160},
        {"name": "Egg Fried Rice", "price": 140},
        {"name": "Gobi Manchuria", "price": 150},
        {"name": "Chicken Manchuria", "price": 180},
        {"name": "Paneer Manchuria", "price": 170},
        {"name": "Chilli Chicken", "price": 190},
        {"name": "Spring Rolls", "price": 120},
        {"name": "Burger", "price": 120},
        {"name": "Chicken Burger", "price": 150},
        {"name": "Veg Pizza", "price": 220},
        {"name": "Chicken Pizza", "price": 280},
        {"name": "French Fries", "price": 100},
        {"name": "Sandwich", "price": 110},
        {"name": "Hot Dog", "price": 130}
    ],

    "Tiffins & Breakfast": [
        {"name": "Idli", "price": 40},
        {"name": "Vada", "price": 40},
        {"name": "Dosa", "price": 50},
        {"name": "Masala Dosa", "price": 70},
        {"name": "Plain Dosa", "price": 50},
        {"name": "Onion Dosa", "price": 60},
        {"name": "Upma", "price": 50},
        {"name": "Poori", "price": 60},
        {"name": "Pongal", "price": 60},
        {"name": "Uttapam", "price": 70},
        {"name": "Rava Dosa", "price": 80}
    ],

    "Cool Drinks & Juices": [
        {"name": "Coca Cola", "price": 40},
        {"name": "Sprite", "price": 40},
        {"name": "Pepsi", "price": 40},
        {"name": "Thumbs Up", "price": 45},
        {"name": "Fanta", "price": 40},
        {"name": "7UP", "price": 40},
        {"name": "Mango Juice", "price": 60},
        {"name": "Orange Juice", "price": 60},
        {"name": "Apple Juice", "price": 70},
        {"name": "Pineapple Juice", "price": 65},
        {"name": "Watermelon Juice", "price": 60},
        {"name": "Lassi", "price": 80},
        {"name": "Buttermilk", "price": 30},
        {"name": "Cold Coffee", "price": 90},
        {"name": "Milkshake", "price": 120}
    ],

    "Curries & Non-Veg": [
        {"name": "Chicken Curry", "price": 180},
        {"name": "Mutton Curry", "price": 250},
        {"name": "Fish Curry", "price": 200},
        {"name": "Prawn Curry", "price": 260},
        {"name": "Butter Chicken", "price": 220},
        {"name": "Chicken Tikka Masala", "price": 210},
        {"name": "Paneer Butter Masala", "price": 160},
        {"name": "Kadai Paneer", "price": 170},
        {"name": "Dal Fry", "price": 120},
        {"name": "Dal Tadka", "price": 130},
        {"name": "Mixed Veg Curry", "price": 140},
        {"name": "Aloo Gobi", "price": 130}
    ]
}

# 🔐 LOGIN
@app.route('/')
def login():
    return render_template('login.html')

# 🏠 RESTAURANTS
@app.route('/dashboard')
def dashboard():
    return render_template('restaurants.html', restaurants=restaurants.keys())

# 🍽️ MENU
@app.route('/menu/<restaurant>')
def menu(restaurant):
    foods = restaurants.get(restaurant, [])
    return render_template('menu.html', foods=foods, restaurant=restaurant)

# 🛒 ADD TO CART
@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    item = request.form['item']
    price = int(request.form['price'])

    for c in cart:
        if c['name'] == item:
            c['quantity'] += 1
            return redirect(url_for('view_cart'))

    cart.append({"name": item, "price": price, "quantity": 1})
    return redirect(url_for('view_cart'))

# 🛍️ CART
@app.route('/cart')
def view_cart():
    total = sum(i['price'] * i['quantity'] for i in cart)
    return render_template('cart.html', cart=cart, total=total)

# ❌ REMOVE
@app.route('/remove/<item>')
def remove(item):
    global cart
    cart = [i for i in cart if i['name'] != item]
    return redirect(url_for('view_cart'))

# 🚚 CHECKOUT
@app.route('/checkout')
def checkout():
    total = sum(i['price'] * i['quantity'] for i in cart)
    return render_template('checkout.html', total=total)

# 🎉 PLACE ORDER
@app.route('/place_order')
def place_order():
    global cart
    total = sum(i['price'] * i['quantity'] for i in cart)
    cart.clear()
    return render_template('order.html', total=total)

# 🚀 RUN
if __name__ == "__main__":
    app.run(debug=True)