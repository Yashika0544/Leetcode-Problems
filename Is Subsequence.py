class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s=list(s)
        c=0
        for i in t:
            try:
                if i==s[c]:
                    c+=1
            except:
                continue
        if c==len(s):
            return True
        return False
