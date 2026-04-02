class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # lmaooo i have no idea i never seen this question 
        # from video do reverse order bc last car will have its speed determined
        stack = []
        pairs = [(p, s) for p,s in zip(position, speed)]
        
        pairs.sort(reverse=True) # sort in reverse order

        for p,s in pairs:
            stack.append((target - p) / s)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
