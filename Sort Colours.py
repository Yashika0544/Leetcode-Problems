class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n=len(nums)
        l=0
        r=n-1
        curr=0
        while(curr<=r):
            if(nums[curr]==2):
                nums[curr],nums[r]=nums[r],nums[curr]
                r-=1
            elif(nums[curr]==1):
                curr+=1
            else:
                nums[curr],nums[l]=nums[l],nums[curr]
                l+=1
                curr+=1
