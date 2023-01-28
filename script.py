import os
import json
import requests

# Chemin vers le dossier archive
path = "./bbc"

# Liste de documents à ajouter à l'index
documents = []

# Parcours les sous-dossiers de archive
for category_folder in os.listdir(path):
    category_path = os.path.join(path, category_folder)
    if os.path.isdir(category_path):
        # Parcours les fichiers dans chaque sous-dossier
        for file_name in os.listdir(category_path):
            file_path = os.path.join(category_path, file_name)
            # Si c'est un fichier texte, on ajoute le document à la liste
            if file_path.endswith(".txt"):
                with open(file_path, "r") as f:
                    text = f.read()
                    documents.append({
                        "category": category_folder,
                        "text": text
                    })

# Formatte les données en respectant le format _bulk
bulk_data = ""
for doc in documents:
    index_data = json.dumps({
        "index": {
            "_index": "articles",
        }
    })
    bulk_data += index_data + "\n" + json.dumps(doc) + "\n"

# Envoie les données en utilisant la méthode _bulk
response = requests.post(
    "http://localhost:9200/articles/_bulk",
    data=bulk_data,
    headers={"Content-Type": "application/x-ndjson"}
)

# Affiche la réponse
print(response.json())
