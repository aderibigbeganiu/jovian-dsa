# Kadane's algorithm

class Solution(object):
    def maxSubArray(self, nums: list[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = []
        arr.append(nums[0])
        maxSum = arr[0]
        for i in range(1, len(nums)):
            arr.append(max(arr[i-1]+nums[i], nums[i]))

            if maxSum < arr[i]:
                maxSum = arr[i]
        return maxSum