class Solution:
    @staticmethod
    def threeSum1(nums: list[int]) -> list[list[int]]:
        lst: list[int] = sorted(nums)
        i, k = (0, len(nums) - 1)
        res: list[list[int]] = []
        j = i + 1
        while i < j and j < k:
            if j >= k:
                i += 1
                j = i + 1
            sum = lst[i] + lst[j] + lst[k]
            if not sum:
                res.append([lst[i], lst[j], lst[k]])
                j += 1
            elif sum > 0:
                k -= 1
            elif sum < 0:
                if sum + lst[k - 1] < 0:
                    i += 1
                    j = i + 1
                else:
                    j += 1
        return res

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        lst = sorted(nums)
        res = []
        i = 0
        while i < len(lst) - 2:
            j, k = i + 1, len(lst) - 1
            while j < k:
                sum_ = sum([lst[i], lst[j], lst[k]])
                if not sum_:
                    new = [lst[i], lst[j], lst[k]]
                    res.append(new)
                if sum_ < 0:
                    j += 1
                    while j < k and lst[j] == lst[j - 1]:
                        j += 1
                else:
                    k -= 1
                    while j < k and lst[k] == lst[k + 1]:
                        k -= 1
            i += 1
            while i < len(lst) - 2 and lst[i] == lst[i - 1]:
                i += 1
        return res


if __name__ == "__main__":
    input: list[list[int]] = [[-1, 0, 1, 2, -1, -4], [0, 1, 1], [0, 0, 0]]
    for lst in input:
        print(Solution().threeSum(lst))
