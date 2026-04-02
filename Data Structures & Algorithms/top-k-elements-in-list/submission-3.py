class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else: d[i]+=1
        d=sorted(d.items(),key=lambda x: x[1], reverse=True)
        return [val[0] for val in d[:k]]
        