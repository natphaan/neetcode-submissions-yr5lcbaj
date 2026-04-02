class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = []

        # have two for loops? that will result in O(n^2)
        # at least itll get the job done



        # watched video solution - honestly very intuitive and smart on saving memory -> i would've made prefix and postfix arrays


        prefix = 1
        postfix = 1

        # want to store the results in an array

        results = [1] * len(nums) # just init to default values of 1 for now


        # let us iterate through nums to get the prefix values 

        for i in range(len(nums)):
            results[i] = prefix
            prefix *= nums[i]
        

        # now iterate back for the postfix


        for i in range(len(nums) -1, -1, -1):
            results[i] *= postfix
            postfix *= nums[i]
        return results






        
        

        
        

        