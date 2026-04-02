class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # first thought is to use a hashmap and store the chars as keys and occurrences as values
        # only lowercase english letters so 26 chars in total

        counts = defaultdict(list)


       

        for str in strs:
            arr = [0] * 26 # same as valid anagram, create an array of 26 0's to count the occurences
            # since we want to use the occurences as keys for our dict, it needs to be immutable so turn it into a tuple
            for char in str:
                arr[ord(char) - ord('a')] += 1 # count the number of occurrences
            # after that make it a key (by turning it into a tuple so immutable)
            key = tuple(arr)

            counts[key].append(str) # add the str as value to key 
        return list(counts.values())
            



        