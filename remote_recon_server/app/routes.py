from flask import Blueprint, request, Response, jsonify
import requests
import csv
import io
import json

main = Blueprint('main', __name__)

@main.route('/reconcile', methods=['POST'])
def reconcile():
    data = request.get_json()
    endpoint1 = data.get('endpoint1')
    endpoint2 = data.get('endpoint2')

    if not endpoint1 or not endpoint2:
        return jsonify({"error": "Both 'endpoint1' and 'endpoint2' are required"}), 400

    try:
        json1 = requests.get(endpoint1).json()
        json2 = requests.get(endpoint2).json()
    except Exception as e:
        return jsonify({"error": f"Failed to fetch or parse JSON: {str(e)}"}), 500

    # Flatten and compare JSON assuming they're lists of dicts
    differences = []
    for i, (item1, item2) in enumerate(zip(json1, json2)):
        for key in set(item1.keys()).union(set(item2.keys())):
            val1 = item1.get(key)
            val2 = item2.get(key)
            if val1 != val2:
                differences.append({
                    "index": i,
                    "field": key,
                    "value_in_endpoint1": val1,
                    "value_in_endpoint2": val2
                })

    # Convert differences to CSV
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=["index", "field", "value_in_endpoint1", "value_in_endpoint2"])
    writer.writeheader()
    for row in differences:
        writer.writerow(row)

    return Response(output.getvalue(), mimetype='text/csv')
