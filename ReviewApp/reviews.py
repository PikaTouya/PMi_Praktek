from flask import Flask, jsonify

app = Flask(__name__)

product_reviews = [
    {"user_id": 1, "product_id": 1, "review": "Sangat Bagus" },
    {"user_id": 2, "product_id": 2, "review": "Good Quality" },
    {"user_id": 3, "product_id": 3, "review": "Kurang Bagus" },
    {"user_id": 4, "product_id": 4, "review": "Terbaikkk" },
]

@app.route('/reviews')
def get_reviews():
    return jsonify(product_reviews)

@app.route('/reviews/<int:product_id>')
def get_reviews_by_id(product_id):
    reviews = [review for review in product_reviews if review['product_id'] == product_id]

    if reviews:
        return jsonify(
            {'product_id': product_id},
            {'reviews' : reviews}
        )
    else:
        return jsonify(
            {'message': 'product not found'},
            404
        )

if __name__ == '__main__':
    app.run(debug=True, port=5003)