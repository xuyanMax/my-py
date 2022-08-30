class NQUEEN:

    def __init__(self, count):
        count = 0

    def solveNQueens(N):
        res = []
        queens = [0] * N

        # queens is a one-dimension array, like [1, 3, 0, 2] means
        # [.Q..]
        # [...Q]
        # [Q...]
        # [..Q.]

        # index represents row number and value represents col number
        def dfs(row):
            if row == len(queens):
                print(queens)
                res.append(queens[:])
                return
            for i in range(len(queens)):
                queens[row] = i
                # check whether nth queen can be placed at column queen[nth_q]
                if valid(row):
                    dfs(row + 1)

        def valid(nth_q):
            for i in range(nth_q):
                if queens[nth_q] == queens[i] or (queens[nth_q] - nth_q) == (queens[i] - i) or (
                        queens[nth_q] + nth_q) == (
                        queens[i] + i):
                    return False
            # RETURN
            return True

        # given queens = [1,3,0,2] this function returns
        # [.Q..]
        # [...Q]
        # [Q...]
        # [..Q.]

        def make_board(queens):
            n = len(queens)
            # [['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.']]
            board = [['.'] * n for _ in range(n)]
            for row, col in enumerate(queens):  # return 0 1; 1 3; 2 0; 3 2
                board[row][col] = 'Q'
            return board

        def make_all_board(res):
            all_board = []
            for queens in res:
                all_board.append(make_board(queens))
            return all_board

        print(queens)
        dfs(0)
        return make_all_board(res)


nqueen = NQUEEN
res = nqueen.solveNQueens(4)
for r in res:
    print(r)
