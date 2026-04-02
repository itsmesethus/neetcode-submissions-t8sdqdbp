class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        cmap={}
        left=0
        max_freq=0
        res=0

        for right in range(len(s)): # iterate through the string s where left and right starts at same point
            cmap[s[right]]=1+cmap.get(s[right],0) # but left stays at 0 and right will slide one by one and get mapped in the dict based one the occurences
            max_freq=max(max_freq,cmap[s[right]]) # max_freq help us to check whether particualr character is repeated more than k

            if (right-left+1)-max_freq > k:
                cmap[s[left]]=cmap[s[left]]-1
                left=left+1
            res=max(res,right-left+1)
        return res
        