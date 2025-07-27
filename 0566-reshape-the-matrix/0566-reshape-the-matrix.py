class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        length = 0
        new_mat = [[0] * c for _ in range(0,r)]
        for row in mat:
            length = max(length, len(row))
        width = len(mat)
        if not width*length == r*c:
            return mat
        mat_r = 0
        mat_c = 0
        for i in range(0,r):
            for j in range(0,c):
                if(mat_c>=length):
                    mat_c = 0
                    mat_r+=1
                new_mat[i][j] = mat[mat_r][mat_c]
                mat_c += 1

        return new_mat
        