class Solution:
    def maxArea(self, coords: List[List[int]]) -> int:
        def findArea(m, max_val, min_val):
            res = 0
            for element in m:
                coord = m[element]
                base = coord[1] - coord[0]
                h = max(max_val - element, element - min_val)
                area = (base * h) / 2
                res = max(res, area)
            return res

        x_map = {} 
        y_map = {}
        max_x = -float('inf')
        max_y = -float('inf')
        min_x = float('inf')
        min_y = float('inf')
        for i in coords:
            x = i[0]
            y = i[1]
            max_x = max(x, max_x)
            max_y = max(y, max_y)
            min_x = min(x, min_x)
            min_y = min(y, min_y)
            if x not in x_map:
                x_map[x] = (y, y)
            else:
                old_min = x_map[x][0]
                old_max = x_map[x][1]
                new_min_y = min(y, old_min)
                new_max_y = max(y, old_max)
                x_map[x] = (new_min_y, new_max_y)
            if y not in y_map:
                y_map[y] = (x, x)
            else:
                old_min = y_map[y][0]
                old_max = y_map[y][1]
                new_min_x = min(x, old_min)
                new_max_x = max(x, old_max)
                y_map[y] = (new_min_x, new_max_x)

        x_val = findArea(x_map, max_x, min_x)
        y_val = findArea(y_map, max_y, min_y)

        if x_val == 0 and y_val == 0:
            return -1
        return int(max(2 * x_val, 2 * y_val))
            
        
# runtime: O(N)
# spacetime: O(N)
