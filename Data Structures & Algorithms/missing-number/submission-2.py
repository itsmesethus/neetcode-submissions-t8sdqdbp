class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        res=n #[1,2,3]
        # it1: say n=3,  3^0^1   ===> here not will be cancelled out.
        #it2: say res=3^0^1,  3^0^1^1^2   ===> '1' will be cancelled out.
        #it3: res=3^0^2, 3^0^2^2^3 ===> '3','2' will be cancelled out
        #so my solution is 0.

        for i in range(len(nums)):
            res=res^(i^nums[i])
        return res

        