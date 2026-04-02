class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        cmap={}
        left=0
        max_freq=0

        for right in range(len(s)):
            cmap[s[right]]=1+cmap.get(s[right],0)
            max_freq=max(max_freq,cmap[s[right]])

            if (right-left+1)-max_freq > k:
                cmap[s[left]]=cmap[s[left]]-1
                left=left+1
        return len(s)-left
        