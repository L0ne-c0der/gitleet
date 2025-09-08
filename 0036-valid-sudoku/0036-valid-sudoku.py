class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[]}
        rows = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[]}
        cells = {'00':[], '01':[], '02':[], '10':[], '11':[], '12':[], '20':[], '21':[], '22':[]}
        
        for i in range(len(board)):
            for j in range(len(board)):
                num = board[i][j]
                cell = str(i//3) + str(j//3)
                if num!='.' and (num in rows[i] or num in cols[j] or num in cells[cell]):
                    return False
                rows[i].append(num)
                cols[j].append(num)
                cells[cell].append(num)
        return True