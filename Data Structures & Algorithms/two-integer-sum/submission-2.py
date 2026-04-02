class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]
        # return []
        map_=[(a,b) for a,b in enumerate(nums)]
        map_.sort(key=lambda x:x[1])
        print(map_)

        left=0
        right=len(nums)-1

        while left<right:
            current_sum=map_[left][1]+map_[right][1]
            if current_sum==target:
                return sorted([map_[left][0],map_[right][0]])
            elif current_sum < target:
                left+=1
            else:
                right-=1
        return []


        
      

            

        