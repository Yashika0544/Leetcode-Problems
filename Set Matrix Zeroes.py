class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return 

        r=len(matrix)
        c=len(matrix[0])
        zr=[0]*r
        zc=[0]*c
        for i in range(r):
            for j in range(c):
                if matrix[i][j]==0:
                    zr[i]=1
                    zc[j]=1
        #for r in zr:
        #    for j in range(c):
        #        matrix[r][j]=0
        #for c in zc:
        #    for i in range(r):
        #        matrix[i][c]=0
        for i in range(r):
            for j in range(c):
                if zr[i] or zc[j]:
                    matrix[i][j]=0
