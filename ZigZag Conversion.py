class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows>=len(s):
            return s
        row=['']*numRows
        f=0
        r=0
        for i in s:
            row[r]+=i
            if r==0:
                f=1
            elif r==numRows-1:
                f=-1
            r+=f
        return ''.join(row)
