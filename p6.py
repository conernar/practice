class Solution1:
    def encode(self, strs: list[str]) -> str:
        res = ""
        for s in strs:
            res += (chr(666) + s)

        return res



    def decode(self, s: str) -> list[str]:
        if s == "":
            return []
        res = []
        temp_str = ""
        for ss in s[1:]:
            if ord(ss) == 666:
                res.append(temp_str)
                temp_str = ""
            else:
                temp_str += ss
        
        res.append(temp_str)
        return res

class Solution:
    def encode(self, strs: list[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        return res


    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        while i < len(s):
            length = 0
            while s[i] != '#':
                length = length * 10 + ord(s[i]) - ord('0')
                i += 1
            i += 1
            res.append(s[i : i + length])
            i += length

        return res



if __name__ == "__main__":
    sol = Solution()
    inputstr = ["hello", " ", "world"]
    encoded_str = sol.encode(inputstr)
    decoded_str = sol.decode(encoded_str)

    print(decoded_str)
