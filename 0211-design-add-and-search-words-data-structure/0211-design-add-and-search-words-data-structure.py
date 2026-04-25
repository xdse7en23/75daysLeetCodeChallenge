class WordDictionary(object):

    def __init__(self):
        self.trie = {}

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['#'] = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def dfs(index, current_dict):
            for i in range(index, len(word)):
                char = word[i]
                
                if char == '.':
                    for child_key in current_dict:
                        if child_key != '#' and dfs(i + 1, current_dict[child_key]):
                            return True
                    return False
                if char not in current_dict:
                    return False
                current_dict = current_dict[char]
                
            return '#' in current_dict

        return dfs(0, self.trie)

