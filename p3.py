class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numbers = {}
        for i in range(len(nums)):
            numbers[nums[i]] = i
        for i in range(len(nums)):
            if target - nums[i] in numbers and i != numbers[target - nums[i]]:
                return [i ,numbers[target - nums[i]]] if i < numbers[target - nums[i]] else [numbers[target - nums[i]], i]

class SolutionElegant:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_dict = {}
        # clean up inelegant implements
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                # complement is seen in a previous iteration,
                # num_dict[complement] is guaranteed to be smaller than i
                return [num_dict[complement], i]
            num_dict[num] = i 
if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([4,2,6], 10))
