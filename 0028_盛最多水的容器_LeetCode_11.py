class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = []
        l = 0
        r = len(height) - 1
        while l != r:
            if height[l] < height[r]:
                res.append((r - l) * height[l])
                l += 1
            else:
                res.append((r - l) * height[r])
                r -= 1
        return max(res)
