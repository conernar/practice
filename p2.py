class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicts, dictt = {}, {}
        for char in s:
            if not dicts.get(char):
                dicts[char] = 1
            else: 
                dicts[char] = dicts[char] + 1

        
        for char in t:
            if not dictt.get(char):
                dictt[char] = 1
            else: 
                dictt[char] = dictt[char] + 1
        
        return dicts == dictt

class SolutionO:
    def isAnagram(self, s: str, t: str) -> bool:
        # optimized code
        if len(s) != len(t):
            return False
        dicts, dictt = {}, {}
        for char in s:
            dicts[char] = dicts.get(char, 0) + 1
        for char in t:
            dictt[char] = dictt.get(char, 0) + 1
        return dictt == dicts
class SolutionP:
    def isAnagram(self, s: str, t: str) -> bool:
        # pythonic way to sovle the problem (colletions.Counter)
        from colletions import Counter
        return Counter(s) == Counter(t)

if __name__ == "__main__":
    sol = Solution()
    print(sol.isAnagram("racecar","carrace"))
    print(sol.isAnagram("qwe123","123qwr"))


