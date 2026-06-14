class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # loop to verify every nine columns:
        for i in range(9):
            seen_row = {}
            seen_col = {}
            for j in range(9):
                if board[i][j] != ".":
                    number_row = ord(board[i][j]) - ord("0")
                    seen_row[number_row] = seen_row.get(number_row, 0) + 1
                    if seen_row[number_row] != 1:
                        return False
                if board[j][i] != ".":
                    number_col = ord(board[j][i]) - ord("0")
                    seen_col[number_col] = seen_col.get(number_col, 0) + 1
                    if seen_col[number_col] != 1:
                        return False
        # 9 blocks
        for n in range(9):
            offset_i = (n * 3) % 9
            offset_j = n // 3 * 3
            seen_block = {}
            for i in range(3):
                for j in range(3):
                    idx_i = offset_i + i
                    idx_j = offset_j + j

                    number = board[idx_i][idx_j]
                    if number != ".":
                        number = ord(number) - ord("0")
                        seen_block[number] = seen_block.get(number, 0) + 1
                        if seen_block[number] != 1:
                            return False
        return True


if __name__ == "__main__":
    sol = Solution()
    board = [
        ["1", "2", ".", ".", "3", ".", ".", ".", "."],
        ["4", ".", ".", "5", ".", ".", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", ".", "3"],
        ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
        [".", ".", ".", "8", ".", "3", ".", ".", "5"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", ".", ".", ".", ".", ".", "2", ".", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "8"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    board2 = [
        ["1", "2", ".", ".", "3", ".", ".", ".", "."],
        ["4", ".", ".", "5", ".", ".", ".", ".", "."],
        [".", "9", "1", ".", ".", ".", ".", ".", "3"],
        ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
        [".", ".", ".", "8", ".", "3", ".", ".", "5"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", ".", ".", ".", ".", ".", "2", ".", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "8"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    print(sol.isValidSudoku(board))
    print(sol.isValidSudoku(board2))
