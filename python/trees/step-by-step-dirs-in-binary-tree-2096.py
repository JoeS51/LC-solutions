# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def getDirection(curr_node, end_value, curr_val):
            if curr_node == None:
                return False
            elif curr_node.val == end_value:
                return True
            curr_val.append("L")
            left = getDirection(curr_node.left, end_value, curr_val)
            if left:
                return True
            curr_val.pop()
            curr_val.append("R")
            right = getDirection(curr_node.right, end_value, curr_val) 
            if right:
                return True
            curr_val.pop()
            return False
        path1 = []
        path2 = [] 
        val = getDirection(root, startValue, path1) 
        val2 = getDirection(root, destValue, path2)
        print(path1)
        print(path2)
        res = ""
        i = 0
        while i < len(path1) and i < len(path2) and path1[i] == path2[i]:
            i += 1
        for j in range(i, len(path1)):
            res += "U"
        for k in range(i, len(path2)):
            res += path2[k]
        return res
        

