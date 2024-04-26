class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for s in strs:
            c=[0]*26
            for co in s:
                c[ord(co)-ord("a")]+=1
            res[tuple(c)].append(s)
        return res.values()
        
