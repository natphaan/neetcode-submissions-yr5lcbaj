class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # did this problem before but don't remember the solution
        # remember to use bucket sort but how??
        # use a hashmap --> thinking about using frequences as key and the num as value

        temp = defaultdict(int) # creates 0 if key doesn't exist
        arr = [[] for i in range(len(nums) + 1)] # +1 so that it goes from 0 to n

        for num in nums:
            temp[num] += 1 # count the number of occurrences

        for num, freq in temp.items(): # take the key value in temp
            arr[freq].append(num) # using the count as index and then the number as value in arr

        result = [] # will be storing the results in here

        # looked at solution but we want to iterate in reverse since at the end should have the most frequences

        for i in range(len(arr) -1, 0, -1):
            for num in arr[i]:
                result.append(num) # add the number to result depening on k freq
                if len(result) == k:
                    return result



    

