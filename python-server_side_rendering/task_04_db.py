import sqlite3
from flask import Flask, render_template, request

def create_database():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
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

if __name__ == '__main__':
    create_database()

app = Flask(__name__)

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
    except Exception as e:
        return None  # Sera géré dans la vue Flask

@app.route('/products')
def display_products():
    source = request.args.get('source')
    error_message = None
    products = []

    if source == "json":
        # (ta logique pour charger via JSON)
        pass
    elif source == "csv":
        # (ta logique pour charger via CSV)
        pass
    elif source == "sql":
        products = read_sqlite()
        if products is None:
            error_message = "Database error: impossible de lire les produits."
    else:
        error_message = "Wrong source"

    return render_template(
        "product_display.html",
        products=products,
        error_message=error_message
    )