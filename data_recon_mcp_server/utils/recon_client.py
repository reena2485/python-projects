import requests
import csv
import io

def call_recon_api(endpoint1: str, endpoint2: str) -> str:
    """
    Sends a POST request to the external reconciliation API with the provided endpoints.
    """
    api_url = "http://127.0.0.1:6000/reconcile"
    payload = {
        "endpoint1": endpoint1,
        "endpoint2": endpoint2
    }
    try:
        response = requests.post(api_url, json=payload)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"
    
