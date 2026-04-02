class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        d=[]
        for i in range(len(nums)):
            if nums[i]==val:
                d.append(i)
        for rev in reversed(d):
            nums.pop(rev)

        return len(nums)
        