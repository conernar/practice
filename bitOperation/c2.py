class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return not bool(n & (n - 1))


if __name__ == "__main__":
    while 1:
        num = int(input())
        print(Solution().isPowerOfTwo(num))
