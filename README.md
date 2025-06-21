import re
from collections import defaultdict
class SimpleIndexer:
    def __init__(self):
        self.index = defaultdict(set)
        self.line_index = defaultdict(list)

    def build_index(self, tokenized_docs):
        self.index.clear()
        for doc_name, tokens in tokenized_docs.items():
            for word in set(tokens):
                self.index[word].add(doc_name)

    def index_lines(self, raw_docs):
        self.line_index.clear()
        for doc_name, content in raw_docs.items():
            lines = content.split('\n')
            for i, line in enumerate(lines, 1):
                cleaned_line = re.sub(r'[\W_]+', ' ', line.lower())
                words = cleaned_line.split()
                for word in words:
                    self.line_index[word].append((doc_name, i, line.strip()))
                     TextAnaSearch — Analyseur de texte et moteur de recherche CLI

TextAnaSearch est un outil modulaire en ligne de commande qui permet d’analyser un ou plusieurs fichiers `.txt`, d’en extraire les mots les plus fréquents, et d’effectuer des recherches précises par mots-clés. Pensé pour la simplicité, la clarté et la modularité.

 Fonctionnalités principales

- 📂 Chargement de fichiers ou dossiers contenant des fichiers `.txt`
- 🧼 Nettoyage et tokenisation automatique (minuscules, suppression de ponctuation)
- 📊 Calcul des fréquences de mots avec affichage des N plus fréquents
- 🔍 Recherche de documents par mots-clés (index inversé)
- 📄 Affichage des lignes contenant les mots-clés
- 💾 Option de sauvegarde des résultats dans un fichier `.txt`

 Architecture modulaire

| Module               | Rôle                                                            |
|----------------------|------------------------------------------------------------------|
| `text_processor.py`  | Chargement, nettoyage, tokenisation des documents               |
| `frequency_analyzer.py` | Analyse fréquentielle des mots                                 |
| `simple_indexer.py`  | Indexation inversée et par ligne                                |
| `document_retriever.py` | Recherche de documents & classement par pertinence             |
| `cli_manager.py`     | Interface utilisateur (menu, interaction, affichage, sauvegarde) |

 Exemple de navigation

```bash
=== TEXTANASEARCH ===
1. Charger des fichiers/dossier
2. Afficher les N mots les plus fréquents
3. Rechercher des documents par mots-clés
4. Quitter

