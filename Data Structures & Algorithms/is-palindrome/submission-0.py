class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # want to have two pointers that start on the beginning and end
        # move the pointers towards each other if the char matches

        # only alphanumeric characters --> have to make a function to determine the alphanumeric
        # what is alphanumeric? --> A to Z, a to z, 0 to 9


        left = 0
        right = len(s) - 1

        while left < right: # the pointers haven't meet yet
            while left < right and not self.alphaNum(s[left]): # the not is for non alphanumeric characters --> if we encounter one, just skip it and move to the next char
                left += 1 ## increment 
            while right > left and not self.alphaNum(s[right]): # same as above
                right -= 1 # decrement

            if s[left].lower() != s[right].lower():
                return False

            ## if it is valid then increment and decrement left and right
            left = left + 1
            right = right - 1

        return True




    def alphaNum(self, c):
        return (ord("A") <= ord(c) <= ord("Z") or ord("a") <= ord(c) <= ord("z") or ord("0") <= ord(c) <= ord("9"))

        

