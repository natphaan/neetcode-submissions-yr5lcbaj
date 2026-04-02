class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # done this question long time ago but i remember we wanted to reach the target


        # create a dict/hashmap to sore the previous numbers if n + diff != target

        previous_nums = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in previous_nums:
                return [previous_nums[diff], i]
            # if this is a new number that is not in the hashmap, then add it
            previous_nums[n] = i
            

        
        