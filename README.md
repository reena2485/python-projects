
FLOW
MCP server -> calls -> remote recon server -> calls -> mock json endppoints

Command to run mock_json_endpoints
python run.py

Command to run remote_recon_server
python run.py


Command to run flask_mcp_server
python run.py


Sample Request to send from terminal to send request to remote_recon_server

curl -X POST http://127.0.0.1:6000/reconcile \
  -H "Content-Type: application/json" \
  -d '{"endpoint1": "http://127.0.0.1:7000/mock1", "endpoint2": "http://127.0.0.1:7000/mock2"}'


Sample POST request to MCP server

 curl -X POST http://127.0.0.1:5000/run-recon \
  -H "Content-Type: application/json" \
  -d '{"endpoint1": "http://127.0.0.1:7000/mock1", "endpoint2": "http://127.0.0.1:7000/mock2"}' \
  -o recon_output.csv



