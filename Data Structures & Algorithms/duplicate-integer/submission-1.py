class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # lets throw this into a set as it will remove any duplicates

        s = set()

        for num in nums:

            # have a check if a duplicate number has been added
            if num in s:
                return True
            s.add(num)
        return False
            

        
        
         