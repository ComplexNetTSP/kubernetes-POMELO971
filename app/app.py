from flask import Flask, request
import socket
from datetime import datetime
from pymongo import MongoClient
import os
import socket

mongo_uri = os.environ.get("MONGO_URI")
client = MongoClient(mongo_uri)

app = Flask(__name__)
db = client.database  # Utilisation de la base de données test_database
save = db.save  # Utilisation de la collection posts

@app.route("/")
def Kubernetes_project():
    hostname = socket.gethostname()
    client_ip = request.remote_addr  # Récupération de l'adresse IP du client
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Créer un dictionnaire avec les informations à insérer
    post_data = {
        "hostname": hostname,
        "client_ip": client_ip,
        "date": current_date
    }

    # Insérer les données dans la collection "posts"
    post_id = save.insert_one(post_data).inserted_id
        
    ten_last_posts = save.find().sort("_id", -1).limit(10)
        
    posts_list = "".join([f"<li>{post['date']} - {post['client_ip']}</li>" for post in ten_last_posts])
    return f"""<p>Name : Antoine LEFEVRE<br>
    projet : Kubernetes-TP<br>
    Version : V2<br>
    Hostname : {hostname}<br>
    Client IP : {client_ip}<br>
    Date : {current_date}<br>
    pod ip : {socket.gethostbyname(socket.gethostname())} <br>
    Document ID: {post_id}</p>
    <h2>10 derniers posts:</h2>
    <ul>{posts_list}</ul>"""

    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
