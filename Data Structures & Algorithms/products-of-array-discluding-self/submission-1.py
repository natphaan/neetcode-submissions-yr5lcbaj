class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # after looking at solution
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        res = [1] * len(nums)
        # naive approach would be to interate through each num 
        #multiplying while ignoring num[i]. This would be n^2 for double loop in same nums list

        # populate the prefix array
        
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]

        # populate the suffix array

        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]

        for i in range(len(nums)):
            res[i] = prefix[i] * suffix[i]
        return res 


            


        