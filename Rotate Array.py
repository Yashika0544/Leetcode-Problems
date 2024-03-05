class Solution:
    def reverse(self,nums,i,j):
        l=i
        r=j
        while l<r:
            temp=nums[l]
            nums[l]=nums[r]
            nums[r]=temp
            l+=1
            r-=1
    def rotate(self, nums: List[int], k: int) -> None:
        k=k%len(nums)
        if k<0:
            k+=len(nums)
        self.reverse(nums,0,len(nums)-k-1)
        self.reverse(nums,len(nums)-k,len(nums)-1)
        self.reverse(nums,0,len(nums)-1)

        

        
