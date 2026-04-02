class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        di=[(k,val) for k,val in enumerate(nums)]
        di.sort(key=lambda x:x[1])
        i=0
        j=len(nums)-1
        while i < j:
            curr_sum=di[i][1]+di[j][1]
            if curr_sum==target:
                return sorted([di[i][0],di[j][0]])
            elif curr_sum < target:
                i+=1
            else: 
                j-=1
        return []
        