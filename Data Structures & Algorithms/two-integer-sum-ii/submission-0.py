class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lookup = {}

        for i, num in enumerate(numbers):
            diff = target - num
            if diff in lookup:
                return [lookup[diff] + 1, i + 1]
            lookup[num] = i
        return None
