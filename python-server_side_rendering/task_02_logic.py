from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route('/items')
def items():
    items_list = []
    # Read and parse items.json
    try:
        json_path = os.path.join(os.path.dirname(__file__), 'items.json')
        with open(json_path, 'r') as f:
            data = json.load(f)
            items_list = data.get('items', [])
    except Exception as e:
        print(f"Error loading items.json: {e}")
        items_list = []

    return render_template('items.html', items=items_list)

# (You can add your previous routes here if you want)
if __name__ == '__main__':
    app.run(debug=True, port=5000)
