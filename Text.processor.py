import os
import re

def lire_fichier(chemin):
    try:
        with open(chemin, 'r', encoding='utf-8') as f:
            return f.read()
    except:
        print(f"[Erreur] Impossible de lire : {chemin}")
        return ""

def lire_dossier(dossier):
    fichiers = [os.path.join(dossier, f) for f in os.listdir(dossier) if f.endswith('.txt')]
    return [lire_fichier(f) for f in fichiers]

def nettoyer_texte(texte):
    texte = texte.lower()
    texte = re.sub(r"[^\w\s]", " ", texte)
    return texte

def tokeniser(texte):
    return re.findall(r"\b\w+\b", texte)

def pretraiter_collection(textes):
    return [tokeniser(nettoyer_texte(t)) for t in textes]



