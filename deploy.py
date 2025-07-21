import subprocess
import sys
import os

def deploy_to_render():
    """Deploy to Render.com using their web interface"""
    print("🚀 Deploying to Render.com...")
    print("1. Go to https://render.com")
    print("2. Sign up with GitHub")
    print("3. Click 'New Web Service'")
    print("4. Connect your GitHub repository")
    print("5. Use these settings:")
    print("   - Build Command: pip install -r requirements.txt")
    print("   - Start Command: python server.py")
    print("   - Environment: Python 3")
    print("6. Deploy!")
    
def deploy_to_railway():
    """Deploy to Railway"""
    print("🚀 Alternative: Deploy to Railway...")
    print("1. Go to https://railway.app")
    print("2. Sign up with GitHub")
    print("3. Click 'Deploy from GitHub repo'")
    print("4. Select your repository")
    print("5. Railway will auto-deploy!")

if __name__ == "__main__":
    print("🔧 FastMCP Deployment Helper")
    print("Choose your deployment method:")
    print("1. Render.com (Free)")
    print("2. Railway.app (Free)")
    
    deploy_to_render()
    print("\n" + "="*50)
    deploy_to_railway()
