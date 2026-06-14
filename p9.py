class Solution:
    def longestConsecutive0(self, nums: list[int]) -> int:
        res = 0
        dic = {}
        for num in nums:
            dic[num] = 1
        for num in nums:
            le = 0
            t = num
            while dic.get(t):
                le += 1
                t += 1
            dic[num] = le
            if le > res:
                res = le
        return res

    def longestConsecutive(self, nums: list[int]) -> int:
        # gracefuly convert nums to a set
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if (num - 1) not in num_set:  # avoid the hidden O(n**2) case elegantly
                length = 1

                while (num + length) in num_set:
                    length += 1

                longest = max(
                    longest, length
                )  # swap values by  max(val1, val2) is a much better pythonic way

        return longest


if __name__ == "__main__":
    input1 = [2, 20, 4, 10, 3, 4, 5]
    input2 = [0, 3, 2, 5, 4, 6, 1, 1]
    sol = Solution()
    print(sol.longestConsecutive(input1))
    print(sol.longestConsecutive(input2))
