#syntax=docker/dockerfile:1

# Utilise une image Python légère comme base
FROM python:3.11-slim

# Définit le répertoire de travail
WORKDIR /app

# Copie les fichiers de l'application dans le conteneur
COPY . .

# Installe les dépendances nécessaires
RUN pip install --no-cache-dir flask


# Définit la commande à exécuter pour démarrer l'application
CMD ["python", "app2.py"]

# Expose le port 5000 (par défaut pour Flask)
EXPOSE 5000
