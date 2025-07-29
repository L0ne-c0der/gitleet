class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        new_mat = [[0]*len(board[0]) for _ in range(len(board))]
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                new_mat[i][j] = board[i][j]

        

        def neighbour_count(r ,c):
            count = 0
            for dr in (-1,0,1):
                for dc in (-1,0,1):
                    if (dr==0 and dc==0):
                        continue
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < m and 0<= nc < n and new_mat[nr][nc]==1):
                       count+=1
            return count

        
        for i in range(m):
            for j in range(n):
                count = neighbour_count(i, j)
                if new_mat[i][j] == 1 and (count<2 or count>3):
                    board[i][j] = 0
                elif new_mat[i][j] == 0 and count==3:
                    board[i][j] = 1
        