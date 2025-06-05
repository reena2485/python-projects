from server import mcp
from utils.recon_client import call_recon_api

@mcp.tool()
def reconcile_data(endpoint1: str, endpoint2: str) -> str:
    """
    Calls an external reconciliation API with two endpoints and returns the result.
    """
    return call_recon_api(endpoint1, endpoint2)
