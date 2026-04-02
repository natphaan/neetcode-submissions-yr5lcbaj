class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # lowkey i have no idea what to do --> the elems do not have to be in consecutive in original array
        # is throwing me off
        # sort the original array? and then see if its consecutive by using two pointers?
        # idk how to use hashmap with this question
        # originally thought of using consecutive runs as keys with values having the actual elem run


        # looked at solution --> had the right idea but i really didn't need to sort

        s = set(nums) # remove all duplicates
        longest = 0 # acc

        for num in s:
            if (num - 1) not in s:
                length = 1 # length of run and its 1 since this is the start of a run
                while (num + length) in s:
                    length += 1
                longest = max(length, longest)
                
        return longest


            

        


