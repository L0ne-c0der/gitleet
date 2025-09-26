class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = {i : set() for i in range(9)}

        cols = {i : set() for i in range(9)}

        cells = {f'{i}{j}' : set() for i in range(9) for j in range(9)}

        for i in range(len(board)):
            for j in range(len(board[0])):
                val = board[i][j]
                if val =='.':
                    continue
                
                cell = str(i//3) + str(j//3)

                if (val in rows[i] or val in cols[j]):
                    return False

                if val in cells[cell]:
                    return False

                rows[i].add(val)
                cols[j].add(val)
                cells[cell].add(val)

        return True