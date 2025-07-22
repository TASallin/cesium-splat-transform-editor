#!/usr/bin/env python3
"""
Setup script for the Cesium SPZ Transform Editor
"""

import subprocess
import sys
import os

def install_requirements():
    """Install Python requirements"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Python requirements installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install requirements: {e}")
        return False

def check_cesium_build():
    """Check if Cesium build files exist"""
    cesium_js = os.path.join("Build", "CesiumUnminified", "Cesium.js")
    if os.path.exists(cesium_js):
        print("✅ Cesium build files found")
        return True
    else:
        print("❌ Cesium build files not found")
        print("   Make sure Build/CesiumUnminified/Cesium.js exists")
        return False

def main():
    print("Setting up Cesium SPZ Transform Editor...")
    print("=" * 50)
    
    success = True
    
    # Check Python version
    if sys.version_info < (3, 7):
        print("❌ Python 3.7 or higher is required")
        success = False
    else:
        print(f"✅ Python {sys.version.split()[0]} detected")
    
    # Install requirements
    if not install_requirements():
        success = False
    
    # Check Cesium build
    if not check_cesium_build():
        success = False
    
    print("=" * 50)
    if success:
        print("✅ Setup complete! Run 'python server.py' to start the application")
        print("   Server will be available at http://localhost:5002")
    else:
        print("❌ Setup failed. Please fix the issues above and try again")
    
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())