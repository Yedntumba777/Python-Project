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
