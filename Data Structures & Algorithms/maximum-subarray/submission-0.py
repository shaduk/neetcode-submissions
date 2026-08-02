class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largestSum = -12828384834
        currentSum = 0
        for num in nums:
            currentSum += num
            largestSum = max(currentSum, largestSum)
            if currentSum < 0:
                currentSum = 0
        return largestSum