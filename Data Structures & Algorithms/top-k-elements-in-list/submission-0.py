class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # my thought process
        # use some sort of hashmap to add all the numbers and
        # iterate through the list to see how many reoccurences and then sort by most frequent?
        # iterating through the array would be O(n) and sorting would take O(log n) at most


        # lets start off by making an empty dict

        # result = {}

        # now want to loop through the list of nums to add to dict
        # the key will be the number and the value will be how many occurences it has appeared in nums

        # for num in nums:
        #     if num in result:
        #         result[num] += 1
        #     else:
        #         result[num] = 1



        # solution: use bucket sort, while modifying the key and value pairs

        # make a hashmap to count the number of occurrences

        count = {}


        # create an empty list that is equal to the length of the nums list

        freq = []

        for i in range(len(nums) + 1): # the + 1 is to account for edge case of max freq, say list is 5 and all 1's then it needs to be in index 5
            freq.append([])

        
        # now lets iterate through the list of nums


        for num in nums:
            count[num] = 1 + count.get(num, 0) # add 1 to the value if already in count, default to 0 if not

        # now iterate through the dict count to add 

        for num, count in count.items(): # need to have two variables to iterate through a dict bc they are pairs
            freq[count].append(num) # basically flipped, the value (of the number of occurrences) is the index for freq



        # create an empty list to store the results of top k elements
        result = []


        # we want to loop through freq, and sort it by desc since it is ordered from least to greatest

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result





    


        

        