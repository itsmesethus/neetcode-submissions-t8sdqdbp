# from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict,Counter
        d={}
        for i in strs:
            d_keys_sorted=''.join(sorted(i))
            if d_keys_sorted not in d:
                d[d_keys_sorted]=[]
            d[d_keys_sorted].append(i)
        return list(d.values())
        