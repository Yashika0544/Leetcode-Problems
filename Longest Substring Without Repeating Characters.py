class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a=set()
        i=0
        res=0
        for j , c in enumerate(s):
            while c in a:
                a.remove(s[i])
                i+=1
            a.add(c)
            res=max(res,j-i+1)
        return res
