class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # d=Counter(nums)
        # dd=d.most_common(k)
        # return [x[0] for x in dd]
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else: d[i]+=1
        d=sorted(d.keys(),key=lambda x: d[x],reverse=True)
        return d[:k]
        
            

        