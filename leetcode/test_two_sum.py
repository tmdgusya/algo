class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # We can use cache that contains value and index.
        # The reason we have to save the index, we have to avoid using same element in array.
        # So, cache is looks like that "{"value" : "index"}"
        cache = {}

        for i in range(0, len(nums)):
            cache[nums[i]] = i
        
        # we can get right value from cache

        for i in range(0, len(nums)):
            right_value = cache.get(target - nums[i])
            if right_value is not None and right_value is not i:
                return [min(i, right_value), max(i, right_value)]
        
        return [-1, -1]
