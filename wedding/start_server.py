#!/usr/bin/env python3
"""
Simple server launcher for the wedding proposal page.
Run this script to start a local web server and automatically open the page in your browser.

Usage: python start_server.py
"""

import http.server
import socketserver
import webbrowser
import os
import socket
import errno
from pathlib import Path

# Configuration
PORT = 8000

# Try to find an available port if 8000 is in use
def find_available_port(start_port=8000, max_attempts=10):
    for port in range(start_port, start_port + max_attempts):
        try:
            # Try to bind to the port
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('', port))
            sock.close()
            return port
        except OSError as e:
            if e.errno == errno.EADDRINUSE:
                continue
            else:
                raise
    raise RuntimeError(f"Could not find an available port between {start_port} and {start_port + max_attempts}")

PORT = find_available_port(8000)

# Get local IP address
def get_local_ip():
    try:
        # Create a socket to determine the local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except:
        return "Unable to determine IP"

# Change to the wedding directory
script_dir = Path(__file__).parent
os.chdir(script_dir)

# Create handler
Handler = http.server.SimpleHTTPRequestHandler

# Get local IP
local_ip = get_local_ip()

# Start server (bind to 0.0.0.0 to allow external connections)
with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
    print("=" * 60)
    print(f"🎉 Wedding Proposal Page Server Started!")
    print("=" * 60)
    print(f"\n📍 Local access: http://localhost:{PORT}")
    print(f"📱 Network access: http://{local_ip}:{PORT}")
    print(f"📁 Serving files from: {script_dir}")
    print("\n✨ Opening page in your browser...")
    print("\n💬 Share the Network URL with others on your WiFi!")
    print("\n⚠️  Press Ctrl+C to stop the server")
    print("=" * 60)
    
    # Open browser
    webbrowser.open(f"http://localhost:{PORT}")
    
    # Keep server running
    print("\n🔴 Server is running. Press Ctrl+C to stop.")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        print("\n\n🛡️ Stopping server...")
        httpd.server_close()
        print("✅ Server stopped successfully!")
        print("👋 Goodbye!\n")
