import os
from text_processor import TextProcessor
from frequency_analyzer import FrequencyAnalyzer
from simple_indexer import SimpleIndexer
from document_retriever import DocumentRetriever

class CLIManager:
    def __init__(self):
        self.processor = TextProcessor()
        self.analyzer = FrequencyAnalyzer()
        self.indexer = SimpleIndexer()
        self.docs = {}
        self.tokens = {}

    def display_menu(self):
        while True:
            print("\n=== TEXTANASEARCH ===")
            print("1. Charger des fichiers/dossier")
            print("2. Afficher les N mots les plus fréquents")
            print("3. Rechercher des documents par mots-clés")
            print("4. Quitter")
            choix = input("Votre choix : ").strip()

            if choix == '1':
                self.load_documents()
            elif choix == '2':
                self.show_top_words()
            elif choix == '3':
                self.keyword_search()
            elif choix == '4':
                print("Au revoir !")
                break
            else:
                print("Choix invalide.")

    def load_documents(self):
        path = input("Chemin du fichier ou dossier à charger : ").strip().strip('"')
        if os.path.isfile(path):
            self.processor.load_file(path)
        elif os.path.isdir(path):
            self.processor.load_folder(path)
        else:
            print("Chemin invalide.")
            return

        self.docs = self.processor.get_documents()
        self.tokens = self.processor.process_documents()
        self.indexer.build_index(self.tokens)
        self.indexer.index_lines(self.docs)
        print(f"{len(self.docs)} document(s) chargé(s) avec succès.")

    def show_top_words(self):
        if not self.tokens:
            print("Aucun document chargé.")
            return
        try:
            n = int(input("Combien de mots fréquents voulez-vous afficher ? "))
            all_tokens = []
            for tokens in self.tokens.values():
                all_tokens.extend(tokens)
            freq = self.analyzer.calculate_frequencies(all_tokens)
            top_words = self.analyzer.get_top_n(freq, n)
            for word, count in top_words:
                print(f"{word}: {count}")
        except ValueError:
            print("Entrée invalide.")

    def keyword_search(self):
        if not self.tokens:
            print("Aucun document chargé. Veuillez d'abord charger des fichiers.")
            return

        keywords = input("Entrez les mots-clés séparés par des espaces : ").lower().strip().split()
        if not keywords:
            print("Aucun mot-clé fourni.")
            return

        retriever = DocumentRetriever(self.indexer.index, self.tokens, self.indexer.line_index)
        results = retriever.query(keywords)

        if results:
            print("\nDocuments trouvés (doc_id : score) :")
            for doc, score in results:
                print(f"{doc}: {score}")
        else:
            print("Aucun document trouvé avec tous les mots-clés fournis.")
            return

        print("\nOccurrences des mots-clés dans les lignes :")
        lines_found = retriever.get_lines_with_keywords(keywords)
        for keyword, doc, line_num, line in lines_found:
            print(f'→ Mot-clé "{keyword}" trouvé dans {doc}, ligne {line_num} : {line}')

        save = input("Souhaitez-vous sauvegarder ces résultats ? (o/n) : ").strip().lower()
        if save == 'o':
            with open("resultats_recherche.txt", "w", encoding="utf-8") as f:
                for keyword, doc, line_num, line in lines_found:
                    f.write(f'→ Mot-clé "{keyword}" trouvé dans {doc}, ligne {line_num} : {line}\n')
            print("Résultats sauvegardés dans 'resultats_recherche.txt'.")