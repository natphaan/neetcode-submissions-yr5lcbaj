class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # for ex 1 it seems 6*6?
        # find the highest left pointer and right pointer

        res = 0
        l = 0
        r = len(heights) - 1


        # edge cases if there are no bars or just one bar
        if len(heights) == 0:
            return 0
        elif len(heights) == 1:
            return 1 * heights[0]

        while l < r:
            area = min(heights[l], heights[r]) * (r-l)
            res = max(res, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res

        
            

            
            
            


        