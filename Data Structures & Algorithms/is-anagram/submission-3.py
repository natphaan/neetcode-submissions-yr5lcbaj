class Solution:
    def isAnagram(self, s: str, t: str) -> bool:


        # want to use the array method

        # since there is only 26 lower case letters, lets init an array of 26


        # lets do a check if the lengths of both strings to see if they are the same

        if len(s) != len(t):
            return False


            # init an array of length 26

        count = [0] * 26

        for i in range(len(s)):
            
            # add each letter occurence to count[] from str s
            count[ord(s[i]) - ord('a')] += 1
            # decrease each letter occurence from str t in count[]
            count[ord(t[i]) - ord('a')] -= 1


        # now iterate through count[] to see if all values are 0, if so, then it is a valid anagram
        for i in count:
            if i != 0:
                return False
        return True



        


        