from flask import Flask
from rest_handler import rest_api_blueprint

app = Flask(__name__)
app.register_blueprint(rest_api_blueprint)

if __name__ == '__main__':
    app.run(debug=True, port=5000)





from flask import Blueprint, request, jsonify

rest_api_blueprint = Blueprint('rest_api', __name__)

@rest_api_blueprint.route('/api/compare', methods=['POST'])
def handle_compare_request():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "Empty or invalid JSON body"}), 400

        print("Received REST Request:")
        print(data)

        # Example: assume the JSON contains 'url1' and 'url2'
        url1 = data.get('url1')
        url2 = data.get('url2')

        if not url1 or not url2:
            return jsonify({"error": "Both 'url1' and 'url2' must be provided"}), 400

        return jsonify({
            "status": "success",
            "message": f"Received two endpoints to compare.",
            "url1": url1,
            "url2": url2
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


flask

curl -X POST http://localhost:5000/api/compare \
-H "Content-Type: application/json" \
-d '{"url1": "http://service-a.com/api", "url2": "http://service-b.com/api"}'
