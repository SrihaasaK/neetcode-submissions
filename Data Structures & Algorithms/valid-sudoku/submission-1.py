class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cs = [set() for _ in range(9)]
        bs = [set() for _ in range(9)]
        rs = [set() for _ in range(9)]
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] != ".":
                    if board[r][c] in rs[r]:
                        return False
                    rs[r].add(board[r][c])
                    if board[r][c] in cs[c]:
                        return False
                    cs[c].add(board[r][c])
                    if board[r][c] in bs[(r//3)*3 + c//3]:
                        return False
                    bs[(r//3)*3 + c//3].add(board[r][c])
        return True

