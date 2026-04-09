class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # what to do??
        # slow and fast pointer?
        # read/write pointer?
        # have one pointer at 0th index
        # have anohter pointer +1 and compare, if the same 

        # set version

        seen = set()

        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        return -1