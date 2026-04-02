class Solution:
    def isPalindrome(self, s: str) -> bool:

        # init thoughts:
        # have two pointers, left and right --> one at start and one at end

        # very rough naive approach

        # l = 0
        # r = len(s) - 1

        # for ch in range(len(s)):
        #     if l == r:
        #         l += 1
        #         r -= 1
        #     return False # if l pointer char is not the same as r pointer char
        # return True

        l = 0
        r = len(s) - 1

        while l < r:
            # skip any non alphanum chars
            if not s[l].isalnum():
                l += 1
                continue
            
            if not s[r].isalnum():
                r -= 1
                continue
            
            # if there is no match then ret false
            if s[l].lower() != s[r].lower():
                return False
            
            # if there is a match, then increment the pointers
            l += 1
            r -= 1
        return True
