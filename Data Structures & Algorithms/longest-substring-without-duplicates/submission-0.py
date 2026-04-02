class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        start=0
        max_len=0

        for idx, val in enumerate(s):
            if val in last_seen and last_seen[val]>=start:
                start=last_seen[val]+1
            last_seen[val]=idx
            max_len=max(max_len, idx-start+1)
        return max_len