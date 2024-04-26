class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n=len(strs)
        if(n==0):
            return " "
        if(n==1):
            return strs[0]
        strs.sort()
        i=0
        end=min(len(strs[0]),len(strs[n-1]))
        while(i<end and strs[0][i]==strs[n-1][i]):
            i+=1
        res=strs[0][:i]
        return res
        
