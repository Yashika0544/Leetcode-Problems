class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        w=s.split(' ')
        d=dict()
        if len(pattern)!=len(w):
            return False
        if len(set(pattern))!=len(set(w)):
            return False
        for i in range(len(w)):
            if w[i] not in d:
                d[w[i]]=pattern[i]
            elif d[w[i]]!=pattern[i]:
                return False
        return True
