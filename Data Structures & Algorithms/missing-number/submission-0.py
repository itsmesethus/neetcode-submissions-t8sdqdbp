class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        natural_sum_nums=n*(n+1)//2
        actual_sum_nums=sum(nums)
        return natural_sum_nums-actual_sum_nums

        