from flask import Flask, jsonify
from flights import flights


app = Flask(__name__)


@app.route('/ping')
def ping():
    return { 'greeting': 'poo'}


@app.route('/flights')
def get_flights():
    return jsonify(flights)


@app.route('/flights/<int:id>')
def get_single_flight(id):
    flight = [element for element in flights if element['flight_id'] == id]
    return flight


if __name__ == '__main__':
    app.run(debug=True)
