class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r=len(matrix)
        c=len(matrix[0])
        def transpose(matrix):
            for i in range(r):
                for j in range(i,c):
                    matrix[i][j],matrix[j][i]=matrix[j][i], matrix[i][j]
        def reverse(matrix):
            for k in range(r):
                l=0
                e=len(matrix)-1
                while l<e:
                    matrix[k][l],matrix[k][e]=matrix[k][e],matrix[k][l]
                    l+=1
                    e-=1
        transpose(matrix)
        reverse(matrix)
        
