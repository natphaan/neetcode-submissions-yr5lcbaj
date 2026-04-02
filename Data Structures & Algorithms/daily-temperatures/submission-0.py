class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:


        # edge case where there is only one temp
        if len(temperatures) == 1:
            return [0]

        res = [0] * len(temperatures)
        stack = [] # from solution --> wan tto make a pair of [temp, index]

        # want i want to do is compare the two elems, if one is larger, then temp increase
        # every pop is a counter? no then we cant backtrack
        # two stacks?

        # for i, temp in enumerate(temperatures):
        #     if stack[i] > stack[i - 1]:
        #         stack.pop()
        #         res.append(i)

                
        #     else:
        #         stack.append(temp)
 

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]: # since these are pairs, we need to access like this
                t, index = stack.pop()
                res[index] = i - index
            stack.append((temp, i))
        return res
        
        