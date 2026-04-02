class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        kth=0

        for i in range(len(nums)):
            if nums[i]!=val:
                nums[kth]=nums[i]
                kth+=1

        return kth
        