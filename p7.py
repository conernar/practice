class Solution0:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = []
        zeroes = 0
        idx = -1
        total = 1
        for i,num in enumerate(nums):
            if num == 0:
                zeroes += 1
                idx = i
            else:
                total = total * num
        if zeroes > 1:
            return [0] * len(nums)
        elif zeroes == 1:
            res = [0] * len(nums)
            res[idx] = total
            return res
        else:
            for num in nums:
                res.append(total // num)
        return res

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # not using the division operation
        n = len(nums)
        res = [1] * n
        prefix = 1
        for i, num in enumerate(nums):
            res[i] = prefix
            prefix *= num
        suffix = 1
        for i in range(n):
            res[n - 1 - i] *= suffix
            suffix *= nums[n - 1 - i]
        return res
            
            


if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,4,6]
    nums2 = [-1,0,1,2,3]

    print(sol.productExceptSelf(nums))
    print(sol.productExceptSelf(nums2))
