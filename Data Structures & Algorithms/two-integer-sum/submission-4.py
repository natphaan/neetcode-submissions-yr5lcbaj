class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # if target - num isn't in the hashmap, then add it
        # if it is, then return the indices of that hashmap

        temp = dict()

        for i, num in enumerate(nums): # enumerate so we can get a counter
            diff = target - num
            if diff in temp: # check to see if the diff is already in hashmap, if not then add to hashmap
                return [temp[diff], i]
            temp[num] = i # since not hashmap we add it

                
        





        