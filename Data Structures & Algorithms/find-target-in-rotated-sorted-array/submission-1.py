class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1

        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid

            if nums[left]<=nums[mid]: # left half is sorted
                if nums[left]<=target<nums[mid]:# if my target lies between ( near left and mid) decrease the right
                    right=mid-1
                else:
                    left =mid+1# if my target lies between (left and near mid) increase the left
                  
            elif nums[mid]<nums[right]:# right half is sorted
                if nums[mid]<target<=nums[right]: # if my target lies between ( mid and near right) increase left
                    left=mid+1
                else: # if my target lies betwen (near mid and right)decrease right
                    right=mid-1
        return -1
        