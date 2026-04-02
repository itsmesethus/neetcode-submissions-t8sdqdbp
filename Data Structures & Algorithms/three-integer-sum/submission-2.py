class Solution:
    def threeSum(self, nums):
        res=set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    sums=nums[i]+nums[j]+nums[k]
                    if sums==0:
                        vals=tuple(sorted((nums[i],nums[j],nums[k])))
                        res.add(vals)
        return [list(x) for x in res]