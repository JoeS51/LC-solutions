# can have duplicate points so a set doesn't work?
# potential datastructures to store points:
# - one for keeping track of duplicate points 
#       (1,1): 2
# - one map for x:set(y) (this helps to find a point on the same x)
# - one map for y:set(x) (this helps to find a point on the same y)
# to find diagonal point find it after you find points on the x and y

# for example:
# (3,10), (11, 2), (3, 2)
# add [11, 10]
# you find (11, 2) and (3, 10) which are both 8 distance so it works
# the last point that works for diagonal has to be [11-8, 10-8] = [3, 2]


class DetectSquares(object):

    def __init__(self):
        self.points = {}
        self.x_map = {}
        self.y_map = {}
        self.num_points = 0
        

    def add(self, point):
        """
        :type point: List[int]
        :rtype: None
        """
        self.num_points += 1
        x = point[0] 
        y = point[1]
        new_point = (x, y)
        if new_point not in self.points:
            self.points[new_point] = 0
        self.points[new_point] += 1
        if x not in self.x_map:
            self.x_map[x] = set()
        self.x_map[x].add(y)
        if y not in self.y_map:
            self.y_map[y] = set()
        self.y_map[y].add(x)
        
    # def count(self, point):
    #     curr_x, curr_y = point
    #     total_squares = 0
    
    #     for y2 in self.x_map.get(curr_x, []):
    #         if y2 == curr_y:
    #             continue  # skip same point
    #         dist = y2 - curr_y
    
    #         # Two possible x-values for square: curr_x ± dist
    #         for dx in [dist, -dist]:
    #             x2 = curr_x + dx
    #             p1 = (curr_x, y2)         # vertically aligned
    #             p2 = (x2, curr_y)         # horizontally aligned
    #             p3 = (x2, y2)             # diagonal corner
    
    #             total_squares += (
    #                 self.points.get(p1, 0) *
    #                 self.points.get(p2, 0) *
    #                 self.points.get(p3, 0)
    #             )
    
    #     return total_squares
    

    def count(self, point):
        """
        :type point: List[int]
        :rtype: int
        """
        curr_x = point[0]
        curr_y = point[1]
        curr_pt = (curr_x, curr_y)
        if curr_x not in self.x_map or len(self.x_map[curr_x]) == 0: 
            return 0
        if curr_y not in self.y_map or len(self.y_map[curr_y]) == 0: 
            return 0
        total_squares = 0
        for possible_y in self.x_map[curr_x]:
            
            if possible_y == curr_y: 
                continue
            check_point = (curr_x, curr_y)
            possible_point = (curr_x, possible_y)
            dist = possible_y - curr_y 
            option1_point = (curr_x + dist, curr_y)
            option2_point = (curr_x - dist, curr_y)
            total_squares += self.check_valid_square(check_point, possible_point, option1_point)
            total_squares += self.check_valid_square(check_point, possible_point, option2_point)
        return total_squares

    def check_valid_square(self, pointCorner, pointTop, pointSide):
        all_x = self.y_map[pointCorner[1]]
        if pointSide[0] not in all_x:
            return 0
        # just need to find diagonal
        diagonal_point = (pointSide[0], pointTop[1])
        if diagonal_point not in self.points:
            return 0
        num_corner = self.points[diagonal_point]
        num_top = self.points[pointTop]
        num_side = self.points[pointSide]
        return num_corner * num_top * num_side

        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)

