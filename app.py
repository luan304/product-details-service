from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

products = ["Laptop Pro", "Wireless Mouse", "Keyboard", "Monitor"]

dealers = {
    "Laptop Pro": ["TechStore A", "Gadget Hub", "ElectroMart"],
    "Wireless Mouse": ["Accessory World", "TechStore A"],
    "Keyboard": ["Gadget Hub", "ElectroMart"],
    "Monitor": ["TechStore A", "Accessory World", "Gadget Hub"]
}

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "OK", "service": "product-details"})

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/getdealers/<product_name>', methods=['GET'])
def get_dealers(product_name):
    dealer_list = dealers.get(product_name, [])
    return jsonify({"dealers": dealer_list})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
