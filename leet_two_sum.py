class Solution(object):
    def twoSum(self, nums: list[int], target: int) -> tuple[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: tuple[int]
        """
        for i in range(len(nums)-1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j

print(Solution().twoSum([2,7,11,15], 18))