from flask import Blueprint, request, jsonify
import requests
import csv
import io

main = Blueprint('main', __name__)

RECON_ENDPOINT = "http://127.0.0.1:6000/reconcile"

@main.route('/run-recon', methods=['POST'])
def run_recon():
    data = request.get_json()
    endpoint1 = data.get('endpoint1')
    endpoint2 = data.get('endpoint2')

    if not endpoint1 or not endpoint2:
        return jsonify({"error": "Both 'endpoint1' and 'endpoint2' are required"}), 400

    recon_response = requests.post(RECON_ENDPOINT, json={
        "endpoint1": endpoint1,
        "endpoint2": endpoint2
    })

    if recon_response.status_code != 200:
        return jsonify({"error": "Failed to get recon data"}), 500

    csv_output = recon_response.text
    return (
        csv_output,
        200,
        {
            'Content-Type': 'text/csv',
            'Content-Disposition': 'attachment; filename="recon_output.csv"'
        }
    )
