from collections import Counter

class FrequencyAnalyzer:
    def _init_(self):
        pass

    def calculate_frequencies(self, tokens):
        counter = Counter(tokens)
        return dict(counter)

    def get_top_n(self, frequency_dict, n):
        sorted_items = sorted(frequency_dict.items(), key=lambda item: item[1], reverse=True)
        return sorted_items[:n]
