class Solution:
    def hammingWeight(self, n: int) -> int:
        """Write a function that
        takes an integer n and returns the number of 1 bits in its binary representation.
        """
        # 11 = (0000,1011)B
        # i = 2 ->     10
        # i - 1 ->      1
        count = 0
        i = 1
        while i <= n:
            if n & i:
                count += 1
            i <<= 1
        return count


if __name__ == "__main__":
    test_lst = [11, 128, 0]
    for n in test_lst:
        print(Solution().hammingWeight(n))
