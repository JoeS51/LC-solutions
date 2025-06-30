# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = {}
        min_lvl = float('inf')
        max_lvl = -float('inf')
        def bfs(root):
            nonlocal levels
            nonlocal min_lvl
            nonlocal max_lvl
            q = deque()
            q.append((root, 0))
            while q:
                curr_node, curr_level = q.popleft()
                min_lvl = min(min_lvl, curr_level)
                max_lvl = max(max_lvl, curr_level)
                if curr_level not in levels:
                    levels[curr_level] = []
                levels[curr_level].append(curr_node.val)
                if curr_node.left:
                    q.append((curr_node.left, curr_level - 1))
                if curr_node.right:
                    q.append((curr_node.right, curr_level + 1))

        if not root:
            return [] 
        bfs(root)

        res = []
        for i in range(min_lvl, max_lvl+1):
            res.append(levels[i])
        return res
        
