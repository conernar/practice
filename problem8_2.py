import re

class SolutionRegex:
    def myAtoi(self, s: str) -> int:
        # Pattern explanation:
        # ^     : match from the beginning of the string
        # \s*   : match zero or more whitespaces (handles leading spaces)
        # (     : start capturing group
        #   [+-]?: optionally match a single '+' or '-' sign
        #   \d+  : match one or more digits
        # )     : end capturing group
        match = re.match(r'^\s*([+-]?\d+)', s)
        
        if not match:
            return 0
            
        # Get the captured digits and sign, and convert to integer
        res = int(match.group(1))
        
        # Clamp to 32-bit signed integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        return max(INT_MIN, min(INT_MAX, res))


class SolutionClean:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
            
        sign = 1
        i = 0
        
        # Handle sign
        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1
            
        res = 0
        # Loop only over remaining digits
        while i < len(s) and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1
            
        # Apply sign and clamp using Python's min() and max()
        res = sign * res
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        return max(INT_MIN, min(INT_MAX, res))


if __name__ == "__main__":
    sol_regex = SolutionRegex()
    sol_clean = SolutionClean()
    
    test_cases = ["42", "   -42", "4193 with words", "words and 987", "-91283472332"]
    
    print("--- Testing Regex Solution ---")
    for tc in test_cases:
        print(f"myAtoi({repr(tc)}) -> {sol_regex.myAtoi(tc)}")
        
    print("\n--- Testing Clean Loop Solution ---")
    for tc in test_cases:
        print(f"myAtoi({repr(tc)}) -> {sol_clean.myAtoi(tc)}")
