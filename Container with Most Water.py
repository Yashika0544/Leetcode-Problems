class Solution:
    def maxArea(self, height: List[int]) -> int:
        res =0
        l=0
        r=len(height)-1
        while l<r:
            ar=(r-l)*min(height[l],height[r])
            res=max(res,ar)
            if height[l]<height[r]:
                l+=1
            elif height[l]>height[r]:
                r-=1
            else:
                r-=1
        return res
