class Solution:
    def myAtoi(self, s:str) -> int:

        #implements the function about convert a string to a 32 bit signed digits
        res = 0
        sign = 0
        s = s.lstrip()
        for char in s:
            if char.isdigit():
                if sign == 0:
                    sign = 1
                res = res * 10 + int(char) - int('0')
            elif (char == '-' or char == '+') and sign == 0:
                sign = -1 if char == '-' else 1
            else:
                break
        res = res * sign
        if res < -2**31:
            return -2**31
        if res > 2**31 - 1:
            return 2**31 - 1
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.myAtoi("-042"))
