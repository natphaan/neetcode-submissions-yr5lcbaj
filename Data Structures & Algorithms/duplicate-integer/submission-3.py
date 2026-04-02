class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # use set to remove duplicates
        s = set()

        for num in nums:
            if num not in s:
                # add to set
                s.add(num)
            else:
                return True
        return False
            
        