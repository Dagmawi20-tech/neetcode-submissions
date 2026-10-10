class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        column = [set() for _ in range(9) ]
        box = [set() for _ in range(9)]
        for i in range(len(board)):
            for j in range(len(board[i])):
                val = board[i][j]
                if val == ".":
                    continue
                b = (i//3) * 3 + (j//3)
                if val not in row[i] and val not in column[j] and val not in box[b]:
                    row[i].add(val)
                    column[j].add(val)
                    box[b].add(val)
                else:
                    return False
        return True


        