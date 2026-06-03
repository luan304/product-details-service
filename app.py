from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

products = {
    "1": {"id": "1", "name": "Laptop Pro", "description": "High performance laptop", "price": 999.99, "category": "Electronics", "stock": 50},
    "2": {"id": "2", "name": "Wireless Mouse", "description": "Ergonomic wireless mouse", "price": 29.99, "category": "Accessories", "stock": 200}
}

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "OK", "service": "product-details"})

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(list(products.values()))

@app.route('/products/<product_id>', methods=['GET'])
def get_product(product_id):
    product = products.get(product_id)
    if product:
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
