class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        se=set(nums)
        longest_streak=0
  

        for i in nums:
            if (i-1) not in nums:
                curr_num=i
                curr_streak=1

                while (curr_num+1) in se:
                    curr_num+=1
                    curr_streak+=1
                longest_streak=max(longest_streak,curr_streak)
        return longest_streak


        