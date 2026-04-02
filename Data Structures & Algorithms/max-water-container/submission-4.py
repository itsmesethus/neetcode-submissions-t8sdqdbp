class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # app1: brute force
        # max_water=0
        # for i in range(len(heights)):
        #     for j in range(i+1,len(heights)):  # cap(rectangle area = length * width)
        #         water_cap= min(heights[i],heights[j]) * (j-i)
        #         max_water=max(max_water,water_cap)
        # return max_water

        # app2: two pointer:
        max_water=0
        left, right= 0 , len(heights)-1

        while left < right:
            water_cap=min(heights[left],heights[right])*(right-left)
            max_water=max(water_cap, max_water)

            if heights[left]<heights[right]:
                left+=1
            elif heights[left]>=heights[right]:
                right-=1
            # else:
            #     right-=1
        return max_water

            

        
