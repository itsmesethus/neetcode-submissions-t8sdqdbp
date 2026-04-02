class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        #app1:
        nums_set=set(nums)
        longest_streak=0

        for i in nums:
            if (i-1) not in nums_set:
                current_streak=1
                current_num=i

                while (current_num+1) in nums_set:
                    current_num+=1
                    current_streak+=1
                longest_streak=max(current_streak, longest_streak)
        return longest_streak
        