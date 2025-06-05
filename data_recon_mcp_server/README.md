Dependencies to install
uv add "mcp[cli]" Flask requests


#How to run data recon mcp server
uv run main.py

Claude MCP server config

{
    "mcpServers": {
      "data_recon_mcp_server": {
        "command": "uv",
        "args": [
          "--directory",
          "/Users/reenaupadhyay/code/python/python-projects/data_recon_mcp_server",
          "run",
          "main.py"
        ]
      }
    }
}    


Note - uv should be available in your system path library, if claude is facing issue to connect to mcp server the check
which uv

let's say it returns - /Users/reenaupadhyay/.local/bin/uv , claude doesn't have access to run uv command

create a symlink

sudo ln -s /Users/reenaupadhyay/.local/bin/uv /usr/local/bin/uv


instead of uv you can use python command also, like
{
  "mcpServers": {
    "recon_mcp_server": {
      "command": "python3",
      "args": ["main.py"],
      "cwd": "/Users/reenaupadhyay/code/recon_mcp_server"
    }
  }
}


Sample prompt to give in claude:

Reconcile the data between the following two endpoints:
http://127.0.0.1:7000/mock1 and http://127.0.0.1:7000/mock2
