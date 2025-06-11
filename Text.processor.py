import os

def lire_textes(dossier):
    textes = []
    for fichier in os.listdir(dossier):
        if fichier.endswith(".txt"):
            chemin = dossier + "/" + fichier
            with open(chemin, "r", encoding="utf-8") as f:
                textes.append(f.read())
    return textes
import re

# Convertir en minuscules
def en_minuscule(texte):
    return texte.lower()

# Supprimer la ponctuation de base
def retirer_ponctuation(texte):
    return re.sub(r"[^\w\s]", " ", texte)

# Découper le texte en mots (tokenisation)
def decouper_mots(texte):
    return texte.split()

# Nettoyage complet : minuscule + suppression ponctuation + découpe
def nettoyer(texte):
    texte = en_minuscule(texte)
    texte = retirer_ponctuation(texte)
    return decouper_mots(texte)
def nettoyer_collection(liste_textes):
    return [nettoyer(txt) for txt in liste_textes]
import re

def nettoyage_avance(texte):
    texte = texte.lower()                         # mise en minuscules
    texte = re.sub(r"https?://\S+", "", texte)    # supprime les URL
    texte = re.sub(r"\d+", "", texte)             # supprime les chiffres
    texte = re.sub(r"[^\w\s]", " ", texte)        # supprime ponctuation
    texte = re.sub(r"\s+", " ", texte).strip()    # espaces multiples
    return texte.split()                          # découpe en mots
def lire_fichier_avec_encodages(fichier):
    try:
        with open(fichier, "r", encodage="mathematiques-8") as f:
            return f.read()
    except UnicodeDecodeError:
        with open(fichier, "r", encodage="latin-1") as f:
            return f.read()
