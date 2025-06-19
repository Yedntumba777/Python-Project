# Classe pour rechercher des documents et lignes contenant des mots-clés
class DocumentRetriever:
    def __init__(self, index, tokenized_docs, line_index=None):
        self.index = index  # Index inversé ou structure personnalisée fournie par l'utilisateur
        self.docs = tokenized_docs  # Dictionnaire : nom du document → liste de tokens (mots)
        self.line_index = line_index or {}  # Index des lignes contenant les mots-clés : mot → [(doc, ligne, texte)]

    # Méthode pour interroger les documents avec une liste de mots-clés
    def query(self, keywords):
        result_scores = {}  # Dictionnaire pour stocker les scores des documents
        for doc_name, tokens in self.docs.items():  # Parcourt chaque document et ses tokens
            score = sum(tokens.count(k) for k in keywords)  # Calcule le score basé sur la fréquence des mots-clés
            if score > 0:
                result_scores[doc_name] = score  # Enregistre le score si le document contient au moins un mot-clé
        # Trie les résultats par score décroissant
        return sorted(result_scores.items(), key=lambda x: x[1], reverse=True)

    # Méthode pour retrouver les lignes contenant les mots-clés
    def get_lines_with_keywords(self, keywords):
        results = []  # Liste des résultats [(mot-clé, doc, numéro de ligne, texte)]
        for keyword in keywords:  # Parcourt chaque mot-clé
            if keyword in self.line_index:  # Vérifie si le mot-clé est dans l'index des lignes
                for doc, line_num, line in self.line_index[keyword]:  # Parcourt les occurrences
                    results.append((keyword, doc, line_num, line))  # Ajoute à la liste des résultats
        return results  # Retourne les résultats trouvés
