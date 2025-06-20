import os  # Module pour interagir avec le système de fichiers
import re  # Module pour les expressions régulières, utile pour le nettoyage de texte

# Définition d'une classe pour gérer le traitement de texte
class TextProcessor:
    def __init__(self):
        self.documents = {}  # Dictionnaire pour stocker le contenu des fichiers
        self.tokens = {}     # Dictionnaire pour stocker les mots tokenisés (nettoyés)

    # Méthode pour charger un fichier texte
    def load_file(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:  # Ouvre le fichier en lecture
                content = f.read()  # Lit tout le contenu
                self.documents[file_path] = content  # Stocke le contenu dans le dictionnaire
                return content  # Retourne le contenu du fichier
        except Exception as e:  # En cas d'erreur lors de l'ouverture du fichier
            print(f"Erreur lors du chargement du fichier {file_path} : {e}")
            return None  # Retourne None si une erreur s’est produite

    # Méthode pour charger tous les fichiers .txt d’un dossier
    def load_folder(self, folder_path):
        count = 0  # Compteur de fichiers chargés avec succès
        for filename in os.listdir(folder_path):  # Parcourt tous les fichiers dans le dossier
            file_path = os.path.join(folder_path, filename)  # Crée le chemin complet
            if os.path.isfile(file_path) and filename.endswith('.txt'):  # Vérifie que c’est un fichier texte
                if self.load_file(file_path):  # Tente de charger le fichier
                    count += 1  # Incrémente si succès
        return count  # Retourne le nombre de fichiers chargés

    # Méthode pour nettoyer un texte et le découper en mots (tokenisation)
    def clean_and_tokenize(self, text):
        text = text.lower()  # Met le texte en minuscules
        text = re.sub(r'[\W_]+', ' ', text)  # Supprime la ponctuation et les caractères spéciaux
        return text.split()  # Découpe le texte en liste de mots

    # Traite tous les documents chargés en les nettoyant et tokenisant
    def process_documents(self):
        self.tokens = {}  # Réinitialise le dictionnaire de tokens
        for path, content in self.documents.items():  # Parcourt chaque document
            self.tokens[path] = self.clean_and_tokenize(content)  # Nettoie et tokenise le contenu
        return self.tokens  # Retourne les documents tokenisés

    # Méthode pour accéder aux documents bruts
    def get_documents(self):
        return self.documents  # Retourne le dictionnaire des documents




