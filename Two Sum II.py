class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1
        s=0
        while l<r:
            s=numbers[l]+numbers[r]
            if s>target:
                r-=1
            elif s<target:
                l+=1
            else:
                return [l+1,r+1]

