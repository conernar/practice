class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        x = abs(x)

        t = 0
        while x > 0:
            t = t*10 + x % 10
            x = x//10
        res = t * sign
        
        if res < -2**31 or res > 2**31 - 1:
            return 0

        return res
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.reverse(12345))

