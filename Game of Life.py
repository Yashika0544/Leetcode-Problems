class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                once=0
                for x in range(max(0,i-1),min(len(board),i+2)):
                    for y in range(max(0,j-1),min(len(board[0]),j+2)):
                        once+=board[x][y] & 1
                if board[i][j]==1 and (once==3 or once==4):
                    board[i][j] |=0b10
                if board[i][j]==0 and once==3:
                    board[i][j] |=0b10
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j]>>=1
