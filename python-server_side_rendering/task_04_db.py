from flask import Flask, render_template, request
import json
import csv
import os
import sqlite3

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
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
    except Exception as e:
        print(f"Error reading CSV: {e}")
    return products

def read_products_sql():
    products = []
    try:
        db_path = os.path.join(os.path.dirname(__file__), 'products.db')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        for row in cursor.fetchall():
            products.append({
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            })
        conn.close()
    except Exception as e:
        print(f"Error reading SQLite DB: {e}")
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    prod_id = request.args.get('id')
    error = None
    data = []

    if source not in ['json', 'csv', 'sql']:
        error = "Wrong source"
        return render_template('product_display.html', error=error)

    if source == 'json':
        data = read_products_json()
    elif source == 'csv':
        data = read_products_csv()
    elif source == 'sql':
        data = read_products_sql()
    else:
        error = "Wrong source"
        return render_template('product_display.html', error=error)

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
