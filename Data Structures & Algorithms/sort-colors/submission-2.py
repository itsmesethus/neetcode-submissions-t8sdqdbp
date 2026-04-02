class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dct={0:0,1:0,2:0}
        for i in nums:
            dct[i]+=1
        
        idx=0
        for i in dct.keys():
            for _ in range(dct[i]):
                nums[idx]=i
                idx+=1
            
        