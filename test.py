import json
import random

def extract_words(file_path, output_json):
    # Lire le fichier en UTF-16
    with open(file_path, "r", encoding="utf-16") as file:
        lines = file.readlines()
    
    # Extraire les mots avant la première virgule ou le premier point
    words = [line.split(",")[0].split(".")[0] for line in lines]
    
    # Générer un score de positivité aléatoire entre 0 et 1
    word_sentiment = {word: round(random.uniform(-1, 1), 2) for word in words}
    
    # Sauvegarder le dictionnaire en JSON
    with open(output_json, "w", encoding="utf-8") as json_file:
        json.dump(word_sentiment, json_file, ensure_ascii=False, indent=2)
    
    print(f"Fichier JSON enregistré sous {output_json}")

# Exemple d'utilisation
extract_words("dico.dic", "dictionnairE.json")
