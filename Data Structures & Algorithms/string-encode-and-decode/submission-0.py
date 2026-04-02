class Solution:

    def encode(self, strs: List[str]) -> str:


        # had no clue on how to start so had to watch the 
        
        # want to start off with an empty string in case if the list is empty

        result = ""

        # so by encoding, we want to represent the total number of characters for a word, following a hash symbol to tell us that after the hash is the word we are interested in

        for s in strs:
            result += str(len(s)) + "#" + s
            # for ex, food --> 4#food
        return result # after looping through the whole list, return all the words as a string with their count and a #

        

    def decode(self, s: str) -> List[str]:

        # want to add this to a list

        decoded = []

        # also need a pointer to keep track
        i = 0

        while i < len(s): # loop through the string
            # have another pointer
            j = i
            while s[j] != "#":
                j += 1
            
            # once j hits a #

            length = int(s[i:j]) # this gets us the length of the word

            # update the pointer i so that it starts on the actual word, after the number and #
            i = j + 1 # bc j was at the # index
            j = i + length # the start of the word + the length of the word should capture all the whole word now

            decoded.append(s[i:j])
            i = j # so that index i starts at the next word that is in s

        return decoded