# You are given two arrays rowSum and colSum of non-negative integers 
# where rowSum[i] is the sum of the elements in the ith row and colSum[j] 
# is the sum of the elements of the jth column of a 2D matrix. 
# In other words, you do not know the elements of the matrix, 
# but you do know the sums of each row and column.

# Find any matrix of non-negative integers of size 
# rowSum.length x colSum.length that satisfies the rowSum and colSum requirements.

# Return a 2D array representing any matrix that fulfills the requirements. 
# It's guaranteed that at least one matrix that fulfills the requirements exists.

class Solution:
    def restoreMatrix(self, rowSum: list[int], colSum: list[int]) -> list[list[int]]:
        rows: int = len(rowSum)
        cols: int = len(colSum)
        cur_row: int = 0
        cur_col: int = 0
        res: list[list[int]] = [[0 for _ in range(cols)] for _ in range(rows)]

        while cur_row < rows or cur_col < cols:
            if cur_row >= rows:
                res[rows - 1][cur_col] = colSum[cur_col]
                cur_col += 1
                continue
            elif cur_col >= cols:
                res[cur_row][cols - 1] = rowSum[cur_row]
                cur_row += 1
                continue

            value_to_put: int = min(rowSum[cur_row], colSum[cur_col])
            rowSum[cur_row] -= value_to_put
            colSum[cur_col] -= value_to_put
            res[cur_row][cur_col] = value_to_put

            # I write this as this because it's possible that rowSum[cur_row] == colSum[cur_col] and we'll want to move both row and col pointers
            if rowSum[cur_row] == 0:
                cur_row += 1
            if colSum[cur_col] == 0:
                cur_col += 1

        return res