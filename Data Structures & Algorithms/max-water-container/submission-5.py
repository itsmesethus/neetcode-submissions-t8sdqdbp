class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water=0

        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                water_cap=min(heights[i],heights[j])*(j-i)
                max_water=max(max_water,water_cap)
        return max_water