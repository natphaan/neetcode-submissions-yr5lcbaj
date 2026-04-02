class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # use a dictionary?

        # my brute force solution had the idea of using a count and the consecutive num to the right
        # prob would've been O(n^2) time



        # from video --> use a set!

        numSet = set(nums) # should remove any duplicates

        sequence = 0

        # checking when a sequence starts by seeing if they have a "left neighbour"

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1 # the start of a sequence

                # checking the right neighbour now
                while (num + length) in numSet:
                    # since it has a right neighbour, incrememnt length
                    length += 1
                sequence = max(length, sequence) # because it will keep looping through the nums and we want to find the largest sequence
                
        return sequence
                

            
                

    
            
        