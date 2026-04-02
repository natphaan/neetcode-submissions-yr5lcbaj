class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # my init thoughts
        # want to use a hashmap again
        # use hashmap where letters are the key, and the occurences of that letter are the values
        # then use that hashmap to look through t, and see if it uses up all the occurences 

        letters_count = {}

        # use enum?


        # iterate through str s, to get all the characters and the count of it
        for char in s:
            letters_count[char] = letters_count.get(char, 0) + 1

        # now iterate through str t, to check if it has the same amount of occurences and same letters of str s

        for char in t:
            if char in letters_count:
                letters_count[char] -= 1
            else:
                return False


        # now if it is a valid anagram, double check if the values reached to 0 

        for count in letters_count.values():
            if count != 0:
                return False
        

        return True




            




        