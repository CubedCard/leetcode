class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def is_valid(x, y, num):
            for i in range(9):
                if board[i][y] == num or board[x][i] == num:
                    return False
            x0, y0 = x // 3 * 3, y // 3 * 3
            for i in range(3):
                for j in range(3):
                    if board[x0 + i][y0 + j] == num:
                        return False
            return True

        def dfs(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for num in '123456789':
                            if is_valid(i, j, num):
                                board[i][j] = num
                                if dfs(board):
                                    return True
                                board[i][j] = '.'
                        return False
            return True

        dfs(board)

