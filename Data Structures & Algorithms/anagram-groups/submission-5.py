class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct={}
        for i  in strs:
            k=''.join(sorted(i))
            if k not in dct:
                dct[k]=[]
            dct[k].append(i)
        return [list(val) for key, val in dct.items()]
            
                