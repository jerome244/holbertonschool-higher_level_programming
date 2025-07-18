from flask import Flask, render_template, request
import json
import csv
import os

app = Flask(__name__)

def read_products_json():
    try:
        path = os.path.join(os.path.dirname(__file__), 'products.json')
        with open(path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading JSON: {e}")
        return []

def read_products_csv():
    products = []
    try:
        path = os.path.join(os.path.dirname(__file__), 'products.csv')
        with open(path, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convert types to match JSON structure
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
    except Exception as e:
        print(f"Error reading CSV: {e}")
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    prod_id = request.args.get('id')
    error = None
    data = []

    # Validate source
    if source not in ['json', 'csv']:
        error = "Wrong source"
        return render_template('product_display.html', error=error)

    # Read data
    if source == 'json':
        data = read_products_json()
    else:
        data = read_products_csv()

    # Filter by id if provided
    if prod_id is not None:
        try:
            prod_id = int(prod_id)
        except ValueError:
            error = "Product not found"
            return render_template('product_display.html', error=error)
        filtered = [p for p in data if p['id'] == prod_id]
        if not filtered:
            error = "Product not found"
            return render_template('product_display.html', error=error)
        data = filtered

    return render_template('product_display.html', products=data, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
