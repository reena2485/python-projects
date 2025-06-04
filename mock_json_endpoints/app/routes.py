from flask import Blueprint, jsonify

main = Blueprint('main', __name__)

@main.route('/mock1', methods=['GET'])
def mock1():
    return jsonify([
        {"id": 1, "name": "Alice", "score": 95},
        {"id": 2, "name": "Bob", "score": 88}
    ])

@main.route('/mock2', methods=['GET'])
def mock2():
    return jsonify([
        {"id": 1, "name": "Alice", "score": 96},
        {"id": 2, "name": "Bob", "score": 88}
    ])
