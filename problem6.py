class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1 or numRows >= len(s):
            return s 
        
        rows = [ "" ] * numRows
        p = 0
        going_down = False 

        for char in s:
            if p == 0 or p == numRows - 1:
                going_down = not going_down
            
            rows[p] += char
            if going_down:
                p += 1
            else:
                p -= 1
        
        return "".join(rows)



if __name__ == "__main__":

    solution = Solution()
    print(solution.convert(s = "PAYPALISHIRING", numRows = 4))
