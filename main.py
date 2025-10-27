
import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

if __name__ == "__main__":
    print("=" * 60)
    print("🚀 Starting Diia API Server...")
    print("=" * 60)
    
    # Check which mode to run
    mode = sys.argv[1] if len(sys.argv) > 1 else "fastapi"
    
    if mode == "flask":
        print("📦 Starting Flask server (Render mode)")
        print("=" * 60)
        from render_server import flask_app
        import asyncio
        from render_server import on_startup
        
        # Initialize DB
        asyncio.run(on_startup())
        
        # Run Flask server
        port = int(os.getenv("PORT", 8000))
        flask_app.run(host="0.0.0.0", port=port, debug=False)
    else:
        print("⚡ Starting FastAPI server (Development mode)")
        print("📚 API docs: http://localhost:8000/docs")
        print("=" * 60)
        import uvicorn
        from api.main import app
        
        port = int(os.getenv("API_PORT", 8000))
        host = os.getenv("API_HOST", "0.0.0.0")
        
        uvicorn.run(app, host=host, port=port, reload=True)

