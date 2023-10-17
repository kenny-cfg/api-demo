from flask import Flask, jsonify
from flights import flights


app = Flask(__name__)


@app.route('/ping')
def ping():
    return { 'greeting': 'poo'}


@app.route('/flights')
def get_flights():
    return jsonify(flights)


if __name__ == '__main__':
    app.run(debug=True)
