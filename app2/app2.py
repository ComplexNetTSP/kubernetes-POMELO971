from flask import Flask, jsonify
import socket

app = Flask(__name__)

@app.route("/")
def index():
    hostname = socket.gethostname()
    return f"""
        <p>message": "Flask app without database connection!",
        "hostname": {hostname}</p>"""
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
