from flask import Flask
import time
import os
import subprocess
import getpass

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Set your name
    name = "Soorya Subramani"

    # Get system username using getpass as a fallback for os.getlogin()
    try:
        username = os.getlogin()
    except OSError:
        username = getpass.getuser()

    # Get current server time in IST
    server_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    # Run the 'top' command and handle possible errors
    try:
        top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')
    except Exception as e:
        top_output = f"Error executing 'top' command: {e}"

    # Format the output as HTML
    html_content = f"""
    <html>
    <head><title>System Status</title></head>
    <body>
        <h1>Name: {name}</h1>
        <p>Username: {username}</p>
        <p>Server Time (IST): {server_time}</p>
        <pre>{top_output}</pre>
    </body>
    </html>
    """
    return html_content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
