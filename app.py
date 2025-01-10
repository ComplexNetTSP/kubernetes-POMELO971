from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def Kubernetes_project():
    hostname = socket.gethostname()

    return f"""<p>Name : Antoine LEFEVRE
    projet : Kubernetes-TP
    Version : V1
    Hostname : {hostname}
    20/12/2024</p>"""