from flask import Flask, render_template, request
import json, csv

app = Flask(__name__)

def read_json():
    with open("products.json", "r") as file:
        return json.load(file)

def read_csv():
    with open("products.csv", newline="") as file:
        return list(csv.DictReader(file))

@app.route("/products")
def display_products():
    source = request.args.get("source")
    prod_id = request.args.get("id")
    error_message = None

    if source == "json":
        products = read_json()
    elif source == "csv":
        products = read_csv()
        # conversions car tout est texte en CSV
        for prod in products:
            prod["id"] = int(prod["id"])
            prod["price"] = float(prod["price"])
    else:
        error_message = "Wrong source"
        products = []
        return render_template("product_display.html", products=products, error_message=error_message)

    if prod_id:
        try:
            prod_id = int(prod_id)
            filtered = [p for p in products if p.get("id") == prod_id]
            if not filtered:
                error_message = "Product not found"
            products = filtered
        except ValueError:
            error_message = "Invalid id parameter"
            products = []

    return render_template("product_display.html", products=products, error_message=error_message)

if __name__ == "__main__":
    app.run(debug=True)
