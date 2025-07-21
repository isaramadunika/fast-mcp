# FastMCP QuickCalc Server

A simple calculator MCP (Model Context Protocol) server built with FastMCP.

## Features

- **Add Function**: Add two numbers together
- **Subtract Function**: Subtract second number from first number
- **HTTP Transport**: Uses streamable HTTP for easy deployment
- **Cloud Ready**: Deployable to Railway, Render, or other cloud platforms

## Local Development

### Prerequisites
- Python 3.11+
- Virtual environment

### Setup
1. Clone the repository:
```bash
git clone https://github.com/isaramadunika/fast-mcp.git
cd fast-mcp
```

2. Create and activate virtual environment:
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the server:
```bash
python server.py
```

The server will start on `http://0.0.0.0:9000/mcp/`

## Claude Desktop Configuration

Add this to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "quickcalc-mcp-server": {
      "command": "path/to/your/.venv/Scripts/python.exe",
      "args": ["path/to/your/server.py"],
      "cwd": "path/to/your/project",
      "env": {
        "PYTHONPATH": "path/to/your/project"
      }
    }
  }
}
```

## Deployment

### Railway
1. Push to GitHub
2. Go to [Railway](https://railway.app)
3. Connect GitHub account
4. Deploy from repository
5. Update Claude config with Railway URL + `/mcp/`

### Render
1. Go to [Render](https://render.com)
2. Create new Web Service
3. Connect GitHub
4. Build Command: `pip install -r requirements.txt`
5. Start Command: `python server.py`

## Available Tools

- `add(a: int, b: int) -> int`: Add two numbers
- `subtract(a: int, b: int) -> int`: Subtract second number from first

## License

MIT License
