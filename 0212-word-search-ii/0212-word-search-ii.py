class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie = {}
        for word in words:
            node = trie
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node['$'] = word 
        ROWS, COLS = len(board), len(board[0])
        res = []

        def dfs(r, c, parent_dict):
            char = board[r][c]
            curr_dict = parent_dict[char]

            if '$' in curr_dict:
                res.append(curr_dict['$'])
                del curr_dict['$']

            board[r][c] = '#'

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] in curr_dict:
                    dfs(nr, nc, curr_dict)

            board[r][c] = char

            if not curr_dict:
                parent_dict.pop(char)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in trie:
                    dfs(r, c, trie)

        return res
