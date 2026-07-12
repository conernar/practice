class Solution:
    def maxArea(self, heights: list[int]) -> int:
        max_area = 0
        i, j = 0, len(heights) - 1
        while i < j:
            area = min(heights[i], heights[j]) * (j - i)
            if area > max_area:
                max_area = area
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        return max_area


if __name__ == "__main__":
    ip = [[1, 7, 2, 5, 4, 7, 3, 6], [2, 2, 2]]
    for l in ip:
        print(Solution().maxArea(l))
