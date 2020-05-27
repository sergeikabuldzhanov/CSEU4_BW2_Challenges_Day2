class Solution(object):
    def twoSum(self, nums, target):
        # We will have to lookup something here, so we probably need a hash table

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # since we also need to store the data, I will use a dictionary for the lookup
        lookup = {}
        # O(n) for the complexity
        # for a num to be in the solution, there needs to be another num in the array
        # which would be equal to target-num.
        # thus we can use target - num as a key, index as value, and store them in a dict
        # while we are traversing the nums array, if the current num is in the dictionary, it's a solution.
        for index, num in enumerate(nums):
            if num in lookup:
                return index, lookup[num]
            else:
                lookup[target-num] = index
        
print(Solution().twoSum([1,2,30,15], 31))