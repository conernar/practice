class Solution:
    def isPalindrome(self, x: int) -> bool:
        t = x
        y = 0
        while(t > 0):
            y = y * 10 + t%10
            t //= 10
        return x == y

class SolutionOptimized:
    def isPalindrome(self, x: int) -> bool:
        """"the optimized function suggested by gemini
        """
        # Early exits
        if x  < 0 or (x % 10 == 0 and x != 0):
            return 0

        # only reverse half and set the loop condition as x > t
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half *  10 + x%10
            x //= 10
        #split conditions of even digits and odd digits
        return reversed_half == x or x == reversed_half // 10



if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome(1234321))
    print(sol.isPalindrome(12))
