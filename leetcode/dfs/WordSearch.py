class WordSearch(object):
    def sol1(self, board, word):
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word): return True
        return False

    def dfs(self, board, i, j, word):
        if not len(word): # all characters are checked
            return True
        if i < 0 or j < 0 or i == len(board) or j == len(board[0]):
            return False
        if board[i][j] != word[0]:
            return False
        tmp = board[i][j]
        board[i][j] = '#'  # mark it as visited
        exist = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
        board[i][j] = tmp
        return exist
