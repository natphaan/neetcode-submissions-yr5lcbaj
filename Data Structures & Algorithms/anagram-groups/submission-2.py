class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        # use a hashmap again?

        # yes!
        result = defaultdict(list) # for an edge case if count did not exist so default value is a list


        # since it is only of lower case english letters, lets make an array of 26

        # lets loop through the strs to add them onto count

        for s in strs:
            count = [0] * 26

            # now iterate through s to add them to count

            for char in s:
                count[ord(char) - ord('a')] += 1
            
            result[tuple(count)].append(s)
        return result.values()
        


        
        