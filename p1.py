class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
            

if __name__ == "__main__":
    sol = Solution()
    print(sol.hasDuplicate([1,2,3,4]))
    print(sol.hasDuplicate([1,2,33,33]))
