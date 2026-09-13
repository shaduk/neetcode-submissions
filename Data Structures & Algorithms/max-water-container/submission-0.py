class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0 
        right = len(heights) - 1
        currentArea = 0
        maxArea = 0
        while left < right:
            height = min(heights[left], heights[right])
            length = right-left
            currentArea = height*length
            maxArea = max(currentArea, maxArea)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return maxArea