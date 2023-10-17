from flask import Flask, jsonify, request
from flights import flights


app = Flask(__name__)


@app.route('/ping')
def ping():
    return { 'greeting': 'poo'}


@app.route('/flights')
def get_flights():
    return jsonify(flights)


@app.route('/flights/by_from_city/<string:from_city>')
def get_single_flight_by_from_city(from_city):
    flight = [element for element in flights if element['from_city'] == from_city]
    return flight


@app.route('/flights/<int:id>')
def get_single_flight(id):
    flight = [element for element in flights if element['flight_id'] == id]
    return flight


@app.route('/flights', methods=['POST'])
def add_flight():
    flight = request.get_json()
    flights.append(flight)
    return flight


if __name__ == '__main__':
    app.run(debug=True)
