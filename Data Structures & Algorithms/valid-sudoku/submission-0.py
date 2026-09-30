class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ducol=defaultdict(set)
        dusqure=defaultdict(set)
        for col in range(len(board)):
            durow=set()
            for row in range(len(board[col])):
                tar=board[col][row]
                squ=(row // 3)*3 + (col // 3)
                if tar == '.':
                    continue
                if tar in durow or tar in ducol[row] or tar in dusqure[squ]:
                    return False
                durow.add(tar)
                ducol[row].add(tar)
                dusqure[squ].add(tar)
        return True
                