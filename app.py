from flask import Flask
import os
import time
import subprocess

app = Flask(_name_)

@app.route('/htop')
def htop():
    name = "Your Full Name"
    username = os.getlogin()
    server_time = time.strftime('%Y-%m-%d %H:%M:%S')
    top_output = subprocess.getoutput('top -b -n 1')

    return f"""
    <h1>Name: {name}</h1>
    <h2>Username: {username}</h2>
    <h2>Server Time (IST): {server_time}</h2>
    <pre>{top_output}</pre>
    """

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)