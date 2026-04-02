class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = defaultdict(list)

        ## get all the strings in the strs list

        for s in strs:

            ## want to initialize an array with 26 0's since it is limited from a-z
            count = [0] * 26

            ## find the ascii value when iterating. In the end its just gonna be (1,1,0,0,0,1)

            for c in s:
                count[ord (c) - ord ("a")] += 1
            
            ## cannot have a list as a key so we have to turn it into a tuple

            result [tuple(count)].append(s)
        
        return result.values()
        