class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        roots = []
        walked = []
        for i in range(m):
            walked.append([False for j in range(n)])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    roots.append((i, j))
        for root in roots:
            if self.inside(root, walked, word, 1, board, m, n):
                return True
        return False

    def inside(self, root, walked, word, i, board, m, n):
        if i == len(word):
            return True
        c = word[i]
        x, y = root
        walked[x][y] = True
        sons = self.getSons(x, y, m, n, walked, board, c)
        if len(sons) == 0:
            walked[x][y] = False
            return False
        for son in sons:
            if self.inside(son, walked, word, i + 1, board, m, n):
                walked[x][y] = False
                return True
        walked[x][y] = False
        return False

    def canGo(self, xx, yy, m, n, walked, board, c):
        return m > xx >= 0 and n > yy >= 0 and walked[xx][yy] is False and board[xx][yy] == c

    def getSons(self, x, y, m, n, walked, board, c):
        sons = []
        if self.canGo(x - 1, y, m, n, walked, board, c):
            sons.append((x - 1, y))
        if self.canGo(x + 1, y, m, n, walked, board, c):
            sons.append((x + 1, y))
        if self.canGo(x, y - 1, m, n, walked, board, c):
            sons.append((x, y - 1))
        if self.canGo(x, y + 1, m, n, walked, board, c):
            sons.append((x, y + 1))
        return sons
