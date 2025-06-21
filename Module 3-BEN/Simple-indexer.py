import re  # Importe le module 're' pour les expressions régulières
from collections import defaultdict  # Importe defaultdict pour créer des dictionnaires avec des valeurs par défaut

class SimpleIndexer:  # Définition de la classe SimpleIndexer
    def _init_(self):  # Constructeur de la classe
        self.index = defaultdict(set)  # Dictionnaire pour l'index des mots vers les documents (sans doublons)
        self.line_index = defaultdict(list)  # Dictionnaire pour indexer chaque mot avec sa ligne dans le document

    def build_index(self, tokenized_docs):  # Méthode pour construire un index inversé à partir de documents tokenisés
        self.index.clear()  # Vide l'index précédent, s'il existe
        for doc_name, tokens in tokenized_docs.items():  # Parcourt chaque document et sa liste de tokens (mots)
            for word in set(tokens):  # Utilise un ensemble pour éviter les doublons de mots dans un même doc
                self.index[word].add(doc_name)  # Ajoute le nom du document à l'ensemble des documents pour ce mot

    def index_lines(self, raw_docs):  # Méthode pour indexer les lignes de texte contenant chaque mot
        self.line_index.clear()  # Vide l'ancien index des lignes
        for doc_name, content in raw_docs.items():  # Parcourt chaque document et son contenu brut (non tokenisé)
            lines = content.split('\n')  # Sépare le contenu en lignes
            for i, line in enumerate(lines, 1):  # Parcourt chaque ligne avec son numéro (à partir de 1)
                cleaned_line = re.sub(r'[\W_]+', ' ', line.lower())  # Nettoie la ligne (minuscules + suppression ponctuation)
                words = cleaned_line.split()  # Découpe la ligne nettoyée en mots
                for word in words:  # Parcourt chaque mot
                    self.line_index[word].append((doc_name, i, line.strip()))  
                    # Associe à chaque mot une liste de tuples : (nom du doc, numéro de ligne, contenu brut de la ligne)
