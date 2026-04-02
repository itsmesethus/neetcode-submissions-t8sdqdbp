class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #return (len(set(nums))!=len(nums))
        dict_={}
        for i in nums:
            if i not in dict_:
                dict_[i]=1
            else:
                dict_[i]+=1
        if any(val>1 for val in dict_.values()):
            return True
        else: return False

        