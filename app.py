from flask import Flask
import os
import psutil
from datetime import datetime

app = Flask(__name__)

@app.route('/htop')
def htop():
    try:
        # Get system information
        full_name = "Your Full Name"  # Replace with your full name
        username = os.getlogin()
        server_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S IST")
        
        # Get the top command output (simulating this)
        top_output = ''
        for p in psutil.process_iter(['pid', 'name']):
            try:
                top_output += f"PID: {p.info['pid']}, Name: {p.info['name']}\n"
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass  # Skip processes we can't access or are terminated
        
        # If no processes are found, give a message
        if not top_output:
            top_output = "No running processes found or access denied to some processes."

        # Create the response content
        response_content = f"""
        <html>
            <body>
                <h1>System Information</h1>
                <p><strong>Name:</strong> {full_name}</p>
                <p><strong>Username:</strong> {username}</p>
                <p><strong>Server Time (IST):</strong> {server_time}</p>
                <h2>Top Output:</h2>
                <pre>{top_output}</pre>
            </body>
        </html>
        """
        
        return response_content
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == '_main_':
    app.run(host="0.0.0.0", port=8080, debug=True)
