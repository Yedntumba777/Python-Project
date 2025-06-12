import os      # Permet de manipuler les fichiers et dossiers
import re      # Permet d'utiliser les expressions régulières pour nettoyer le texte

# Fonction qui lit un fichier texte en essayant l'encodage UTF-8
def lire_fichier(chemin):
    try:
        with open(chemin, 'r', encoding='utf-8') as f:  # Ouvre le fichier en lecture
            return f.read()  # Retourne tout le contenu sous forme de chaîne de caractères
    except:  # Si une erreur survient (fichier introuvable, encodage invalide...)
        print(f"[Erreur] Impossible de lire : {chemin}")  # Affiche un message d’erreur
        return ""  # Retourne une chaîne vide
        

# Fonction qui parcourt un dossier pour lire tous les fichiers .txt
def lire_dossier(dossier):
    fichiers = [os.path.join(dossier, f) for f in os.listdir(dossier) if f.endswith('.txt')]  
    # Crée une liste des chemins complets vers les fichiers texte
    return [lire_fichier(f) for f in fichiers]  # Retourne une liste de textes lus

# Fonction qui nettoie un texte brut
def nettoyer_texte(texte):
    texte = texte.lower()  # Met tout en minuscules pour homogénéiser
    texte = re.sub(r"[^\w\s]", " ", texte)  # Supprime la ponctuation (ne garde que lettres, chiffres et espaces)
    return texte  # Retourne le texte nettoyé

# Fonction qui découpe le texte propre en mots (tokenisation)
def tokeniser(texte):
    return re.findall(r"\b\w+\b", texte)  # Capture tous les "mots" composés de caractères alphanumériques

# Fonction principale qui applique nettoyage + tokenisation à une collection
def pretraiter_collection(textes):
    return [tokeniser(nettoyer_texte(t)) for t in textes]  # Pour chaque document : nettoie puis tokenise

    



