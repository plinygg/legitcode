# You are given an m x n matrix of characters box representing a side-view of a box. Each cell of the box is one of the following:

# A stone '#'
# A stationary obstacle '*'
# Empty '.'
# The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. 
# Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. 
# Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.

# It is guaranteed that each stone in box rests on an obstacle, another stone, or the bottom of the box.

# Return an n x m matrix representing the box after the rotation described above.

class Solution:
    def rotateTheBox(self, box):
        m = len(box)
        n = len(box[0])
        result = [["" for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                result[i][j] = box[j][i]

        for i in range(n):
            result[i].reverse()

        for j in range(m):
            for i in range(n - 1, -1, -1):
                if (result[i][j] == "."):
                    next_row_with_stone = -1
                    for k in range(i - 1, -1, -1):
                        if result[k][j] == "*":
                            break
                        if (result[k][j] == "#"):
                            next_row_with_stone = k
                            break
                    if next_row_with_stone != -1:
                        result[next_row_with_stone][j] = "."
                        result[i][j] = "#"

        return result

