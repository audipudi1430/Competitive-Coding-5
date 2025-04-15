# Approach:
# 1. Use three hash sets to track seen digits: one for each row, column, and 3x3 sub-box.
# 2. For every cell in the board, skip empty cells. If the digit is already present in the corresponding row, column, or box — it's invalid.
# 3. Otherwise, add the digit to the respective sets. If no conflicts occur during traversal, the board is valid.

# Time Complexity: O(1) — The board size is fixed (9x9), so constant time regardless of input.
# Space Complexity: O(1) — At most 81 elements across rows, columns, and boxes — all bounded by the fixed board size.

from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Use sets to track the seen numbers for each row, column, and 3x3 box
        cols = defaultdict(set)
        rows = defaultdict(set)
        square = defaultdict(set)  # key = (r // 3, c // 3)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue

                if val in rows[r] or val in cols[c] or val in square[(r // 3, c // 3)]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                square[(r // 3, c // 3)].add(val)

        return True
