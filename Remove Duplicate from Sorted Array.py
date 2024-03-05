class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        if(n==0):
            return 0
        else:
            c=0
            p=nums[0]
            for i in range(n):
                if(nums[i]!=nums[c]):
                    c+=1
                    nums[c]=nums[i]
            return c+1
