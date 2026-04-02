class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # return len(set(nums))<len(nums)
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        return any([x>1 for x in d.values()])