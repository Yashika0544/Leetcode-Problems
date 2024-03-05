class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        for num in range(len(nums)):
            if nums[num]!=val:
                nums[i]=nums[num]
                i+=1
        return i
