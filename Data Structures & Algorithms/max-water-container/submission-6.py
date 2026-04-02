class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max_water=0
        left=0
        right=len(heights)-1
        
        while left < right:
            x=heights[left]
            y=heights[right]

            water_container=min(x,y)*(right-left)
            max_water=max(max_water,water_container)

            if heights[left]<heights[right]: left+=1
            else: right-=1
        return max_water
        