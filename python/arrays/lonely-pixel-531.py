# My initial solution 
# O(n^2)
class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        m = len(picture)
        n = len(picture[0])

        rows = [0] * m
        cols = [0] * n

        rows_index = {}
        cols_index = {}

        for i in range(m):
            count = 0
            for j in range(n):
                if picture[i][j] == "B":
                    count += 1
                    rows_index[i] = j
                    rows[i] = count

        for i in range(n):
            count = 0
            for j in range(m):
                if picture[j][i] == "B":
                    count += 1
                    cols_index[i] = j
                    cols[i] = count

        res = 0
        for i in range(m):
            if rows[i] != 1:
                continue
            curr_col = rows_index[i]
            if cols[curr_col] == 1:
                res += 1
        return res
            
# the solution on the editorial just uses the count arrays like i did but iterates
# over the whole thing again and checks between the two arrays
