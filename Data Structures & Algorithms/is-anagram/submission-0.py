class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # lets initialize an empty dictionary to store characters and occurences
        char_count = {}

        for char in s:
            char_count[char] = char_count.get(char, 0) + 1


        # now check iterate through t to check if they have the same

        for char in t:
            if char not in char_count:
                return False
            else:
                char_count[char] -= 1

        
        # check if all counts are zero

        for count in char_count.values():
            if count != 0:
                return False


        return True

              
        