class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # already looked at solution but it is two sum 2 for most of it if we sort array
        # trick is to sort it? --> n log n time


        nums.sort()
        res = []

        for i, n in enumerate(nums):
            # check if nums has more than one num and if its a duplicate

            if i > 0 and n == nums[i - 1]:
                continue
            
            l = i + 1
            r = len(nums) - 1

            while l < r:
                sum = n + nums[l] + nums[r]

                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res




            



        