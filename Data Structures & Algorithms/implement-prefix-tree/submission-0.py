class PrefixTree:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        trie = self.trie
        for c in word:
            if c not in trie:
                trie[c] = {}
            trie = trie[c]
        trie['end'] = 1

    def exists(self, trie, word):
        if(len(word) == 0):
            if('end' in trie):
                return True
            return False
        if(word[0] not in trie):
            return False
        return self.exists(trie[word[0]], word[1:])
    
    def startWith(self, trie, word):
        if(len(word) == 0):
            return True
        if(word[0] not in trie):
            return False
        return self.startWith(trie[word[0]], word[1:])

    def search(self, word: str) -> bool:
        return self.exists(self.trie, word)

    def startsWith(self, prefix: str) -> bool:
        return self.startWith(self.trie, prefix)
        