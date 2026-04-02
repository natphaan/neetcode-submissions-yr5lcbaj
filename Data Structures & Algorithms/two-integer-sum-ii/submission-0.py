class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # two pointers for o(1) space


        

        l = 0
        r = len(numbers) - 1


        while l < r:
            sum = numbers[l] + numbers[r]

            # we know that since it is ordered ascending, if the sum is greater than target, that means we need to move right pointer to the left

            if sum > target:
                r -= 1
            elif sum < target:
                l += 1

            else: # that means that the sum == target so return the indices (+1 since they want 1 indexed)
                return [l + 1, r + 1]
        # if nothing doesn't add up to target, then return empty list
        return []

            
