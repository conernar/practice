class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        lst: list[int] = numbers
        i: int = 0
        j: int = len(lst) - 1
        while i < j:
            # tar: int = target - lst[i]
            sum = lst[i] + lst[j]
            if sum == target:
                return [i + 1, j + 1]
            if sum < target:
                i += 1
            else:
                j -= 1
        return [i + 1, j + 1]


if __name__ == "__main__":
    input, target = [1, 2, 3, 4], 3
    sol: Solution = Solution()
    print(sol.twoSum(input, target))
