class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        def binary_search(target, arr):
            l, r = 0, len(arr)
            while l < r:
                mid = (l + r) // 2
                if arr[mid] < target:
                    l = mid + 1
                else:
                    r = mid
            return l
        
        x_map = {}
        y_map = {}
        for b in buildings:
            x = b[0]
            y = b[1]
            if x not in x_map:
                x_map[x] = [] 
            if y not in y_map:
                y_map[y] = [] 
            y_map[y].append(x)
            x_map[x].append(y)
        
        for y in y_map:
            y_map[y].sort()
        for x in x_map:
            x_map[x].sort()

        count = 0
        for x, y in buildings:
            x_list = y_map[y]
            y_list = x_map[x]
            x_i = binary_search(x, x_list)
            y_i = binary_search(y, y_list)
            if x_i > 0 and x_i < len(x_list) - 1 and y_i > 0 and y_i < len(y_list) - 1:
                count += 1
        return count


