import sqlite3
import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)

def create_database():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS Products")
    cursor.execute('''
        CREATE TABLE Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    cursor.execute('''
        INSERT INTO Products (id, name, category, price) VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')
    conn.commit()
    conn.close()

def read_sqlite():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()
        return [
            {'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]}
            for row in rows
        ]
    except Exception:
        return None  # Cette erreur sera gérée dans la route Flask

def read_json():
    try:
        with open('products.json', 'r') as f:
            return json.load(f)
    except Exception:
        return None

def read_csv():
    try:
        with open('products.csv', newline='') as f:
            products = list(csv.DictReader(f))
            # Conversion des champs id et price qui sont lus en string
            for p in products:
                p['id'] = int(p['id'])
                p['price'] = float(p['price'])
            return products
    except Exception:
        return None

@app.route('/products')
def display_products():
    source = request.args.get('source')
    error_message = None
    products = []

    if source == "json":
        products = read_json()
        if products is None:
            error_message = "Error reading JSON data"
    elif source == "csv":
        products = read_csv()
        if products is None:
            error_message = "Error reading CSV data"
    elif source == "sql":
        products = read_sqlite()
        if products is None:
            error_message = "Database error: impossible de lire les produits."
    else:
        error_message = "Wrong source"

    return render_template(
        "product_display.html",
        products=products if products else [],
        error_message=error_message
    )

if __name__ == "__main__":
    create_database()
    app.run(debug=True, port=5000)
