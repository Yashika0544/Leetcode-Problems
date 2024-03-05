class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans=0
        for x1,y1 in points:
            c=collections.Counter()
            for x2,y2 in points:
                ans+=2*c[(x1-x2)**2 + (y1-y2)**2]
                c[(x1-x2)**2 + (y1-y2)**2]+=1
        return ans
