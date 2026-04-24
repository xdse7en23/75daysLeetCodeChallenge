class Trie(object):

    def __init__(self):
        self.root = {}

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.root
        for char in word:
            if char not in curr:
                curr[char] = {}
            curr = curr[char]
        curr['*'] = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        curr = self.root
        for char in word:
            if char not in curr:
                return False
            curr = curr[char]
        return '*' in curr

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        curr = self.root
        for char in prefix:
            if char not in curr:
                return False
            curr = curr[char]
        return True

