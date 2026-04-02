class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # i want to use a hashmap to store all the chars
        # or make an array of 26 chars


        # first lets check the length of each string to consider if it's an anagram

        if len(s) != len(t):
            return False
        

        # if not then create 26 char array

        arr = [0] * 26

        for char in s:
            arr[ord(char) - ord('a')] += 1
        
        # now subtract from arr of any char's from t. If all 0 then anagram

        for tChar in t:
            arr[ord(tChar) - ord('a')] -= 1
            if arr[ord(tChar) - ord('a')] < 0: # early check if any dip below 0 then automatically not an anagram
                return False
        
        return True

        
        

