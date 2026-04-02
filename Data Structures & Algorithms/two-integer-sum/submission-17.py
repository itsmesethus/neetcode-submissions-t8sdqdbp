class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # new=[(ke,va) for ke,va in enumerate(nums)]
        # new=sorted(new,key=lambda x:x[1])

        # left=0
        # right=len(nums)-1
        # while left <right:
        #     cur_sum=new[left][1]+new[right][1]
        #     if cur_sum==target:
        #         return sorted([new[left][0],new[right][0]])
        #     elif cur_sum < target:
        #         left+=1
        #     else:
        #         right-=1
        # return []

        d={} # val: index

        for ids,vals in enumerate(nums):
            diff = target - vals
            if diff in d:
                return sorted([d[diff],ids])
            d[vals]=ids
        return []
