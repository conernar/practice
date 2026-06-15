class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return bool(n) and not n & (n - 1)


if __name__ == "__main__":
    while 1:
        num = int(input())
        print(Solution().isPowerOfTwo(num))
