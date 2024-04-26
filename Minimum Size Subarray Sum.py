import math 
from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sums=0
        l=0
        r=0
        ans=math.inf
        length=len(nums)
        while(r<length):
            sums+=nums[r]
            while(sums>=target):
                ans=min(r-l+1,ans)
                sums-=nums[l]
                l+=1
            r+=1
        return ans if ans != math.inf else 0           
