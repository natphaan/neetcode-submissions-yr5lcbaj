class Solution:

    def encode(self, strs: List[str]) -> str:

        # lets make a delimiter which helps when a word starts
        # also count the letters and have it 

        result = "" # empty str for now

        for s in strs:
            result += str(len(s)) + "#" + s
        return result

    def decode(self, s: str) -> List[str]:

        result = []
        i = 0

        while i < len(s):
            # have another pointer j so that we can get the length of that specific string
            j = i
            while s[j] != "#":
                j += 1 # increment j until it hits delimiter
            length = int(s[i:j]) # get the int number for length
            i = j + 1 # to get to the first char of string
            j = i + length # to start at the next int for the next string
            result.append(s[i:j])
            i = j
        return result


            
            
