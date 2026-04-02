class Solution:
    def threeSum(self, nums):
        res = set()
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):      # Start from i + 1
                for k in range(j + 1, n):  # Start from j + 1
                    if nums[i] + nums[j] + nums[k] == 0:
                        # Sort them so [-1, 0, 1] and [1, 0, -1] look the same
                        triplet = tuple(sorted((nums[i], nums[j], nums[k])))
                        res.add(triplet)
        
        return [list(x) for x in res]