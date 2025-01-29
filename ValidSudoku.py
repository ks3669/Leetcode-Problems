class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Each of these lists will hold 9 sets, one per row/col/box.
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]  # Each 3x3 box identified by (r//3)*3 + (c//3)

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == '.':  # Skip empty cells
                    continue

                # Check row
                if val in rows[r]:
                    return False
                rows[r].add(val)

                # Check col
                if val in cols[c]:
                    return False
                cols[c].add(val)

                # Identify which box we're in (0..8)
                box_index = (r // 3) * 3 + (c // 3)
                # Check box
                if val in boxes[box_index]:
                    return False
                boxes[box_index].add(val)

        return True
