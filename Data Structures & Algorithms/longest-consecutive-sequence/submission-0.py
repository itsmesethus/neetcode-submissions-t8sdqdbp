class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0: return 0
        else:
            nums.sort()
            high_val=1
            cur_streak=1
            i=0
            while i < len(nums)-1:
                j=i+1
                if nums[j]-nums[i]==1:
                    cur_streak+=1
                    high_val=max(cur_streak,high_val)
                elif nums[i]!=nums[j]:
                    cur_streak=1
                i=j
                
            return high_val
