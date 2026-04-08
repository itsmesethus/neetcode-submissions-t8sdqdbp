class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_stk=0
        crt_stk=0
        for i in nums:
            if i==1:
                crt_stk+=1
                if crt_stk > max_stk:
                    max_stk=crt_stk
            else:
                crt_stk=0
        return max_stk
            

         




        
        