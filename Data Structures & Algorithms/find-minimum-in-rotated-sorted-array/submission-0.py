class Solution:
    def findMin(self, nums: List[int]) -> int:

        nums.sort(reverse=False)
        lf=0
        rg=len(nums)-1

        while lf<=rg:

            mid=(lf+rg)//2

            if nums[mid]==min(nums):
                return nums[mid]
            else:
                if nums[mid]<lf:
                    lf=mid
                else:
                    rg=mid


        