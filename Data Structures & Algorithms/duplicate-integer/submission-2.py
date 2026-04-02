class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:


        s = set()

        for num in nums:


            # if the number is already in s, then return true since duplicate
            if num in s:
                return True
            # if not, then add to s
            s.add(num)

        # if looped through entire list, then there are no duplicates
        return False
            
         