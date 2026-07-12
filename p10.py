class Solution:
    def isPalindrome(self, s: str) -> bool:
        str_lst = list(s.lower())
        i = 0
        j = len(s) - 1 - i
        while i < j:
            while i < len(s) - 1 and not str_lst[i].isalnum():
                i += 1
            while j > 0 and not str_lst[j].isalnum():
                j -= 1
            if (
                str_lst[i].isalnum()
                and str_lst[j].isalnum()
                and str_lst[i] != str_lst[j]
            ):
                return False
            i += 1
            j -= 1
        return True


if __name__ == "__main__":
    input1 = "Was it a car or a cat I saw?"
    input2 = "     "

    sol = Solution()
    print(sol.isPalindrome(input1))
    print(sol.isPalindrome(input2))
