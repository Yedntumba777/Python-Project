from collections import Counter #importe counter pour compter les éléments d'une liste rapidement
#classe qui pernet d'analyser la fréquence des mots ou éléments d'une liste 
class FrequencyAnalyzer:
    def _init_(self):
        pass #constructeur vide (peut être personnalisé plus tard si besoin) 
#fonction pour calculer les fréquences des éléments dans une liste (tokens)
    def calculate_frequencies(self, tokens):
        counter = Counter(tokens) #utilise counter pour compter chaque élément
        return dict(counter)     #convertit le résultat en dictionnaire {élément:fréquence}
#fonction pour obtenir les 'n' éléments les plus fréquents 
    def get_top_n(self, frequency_dict, n):
        #trie les éléments du dictionnaire par fréquence décroissante
        sorted_items = sorted(frequency_dict.items(), key=lambda item: item[1], reverse=True)
        return sorted_items[:n] #retourne les n premiers éléments les plus fréquents 
    