class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        c=0
        while(m<len(nums1)):
            nums1[m]=nums2[c]
            c+=1
            m+=1
        nums1.sort()
        
