class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l=0
        leng=0

        for r in range(len(nums)):
            if nums[r]==0:
                l=r+1
            width=r-l+1
            leng=max(width,leng)
        return leng
        

         




        
        