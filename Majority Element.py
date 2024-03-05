class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c=0
        mE=0
        for i in range(len(nums)):
            if c==0:
                mE=nums[i]
            if mE==nums[i]:
                c+=1
            else:
                c-=1
        return mE
        
