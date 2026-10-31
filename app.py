from flask import Flask, jsonify, request
import time
import random

app = Flask(__name__)

products = {
    "P100": {"name": "Milk", "available": True, "stock": 25},
    "P101": {"name": "Bread", "available": True, "stock": 12},
    "P102": {"name": "Eggs", "available": False, "stock": 0},
    "P103": {"name": "Rice", "available": True, "stock": 40},
}

@app.route("/")
def home():
    return jsonify({
        "service": "Quick-Commerce Product API",
        "status": "running"
    })

@app.route("/product/<product_id>")
def product(product_id):

    # Small artificial delay to simulate real API processing
    time.sleep(random.uniform(0.05, 0.2))

    product = products.get(product_id)

    if product:
        return jsonify({
            "product_id": product_id,
            **product
        })

    return jsonify({
        "product_id": product_id,
        "available": False,
        "message": "Product not found"
    }), 404


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)