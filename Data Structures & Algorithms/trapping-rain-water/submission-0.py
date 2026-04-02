class Solution:
    def trap(self, height: List[int]) -> int:
        # my thoughts so far:
        # left and right pointers 
        # check neighbour of left pointer, if the neighbour is less than left, then water
        # can be trapped
        # vice versa with right pointer
        # how do we increment the pointers?


        res = 0
        l = 0
        r = len(height) - 1
        leftMax = height[l]
        rightMax = height[r]


        # edge cases

        if len(height) == 0:
            return 0
        elif len(height) == 1:
            return 0
        elif len(height) == 2:
            return 0
        

        while l < r:

            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res


        