# This was my trie approach to this question. It works, but it is lengthy because you have to build the trie and then traverse it
# It can be improved by using a simple DFS approach to generate the numbers in lexicographical order
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        class Node:
            def __init__(self):
                self.val = None
                self.children = []
        
        def addNum(i, root):
            s = str(i)
            idx = 0
            while root:
                found = False
                for child in root.children:
                    if child.val == s[idx]:
                        root = child
                        found = True
                        idx += 1
                        break
                if not found:
                    new_node = Node()
                    new_node.val = s[idx]
                    new_node.children = []
                    root.children.append(new_node)
                    root = None
        res = []
        def dfs(root, curr):
            nonlocal res
            if not root:
                return
            if root.val != -1:
                curr += root.val
                res.append(int(curr))
            for child in root.children:
                dfs(child, curr)

        
        root = Node()
        root.val = -1
        root.children = []
        for i in range(1, n+1):
            addNum(i, root)
        
        dfs(root, "")

        return res

        
# Here is a better approach using a simple DFS to generate the numbers in lexicographical order
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        lexicographical_numbers = []
        # Start generating numbers from 1 to 9
        for start in range(1, 10):
            self._generate_lexical_numbers(start, n, lexicographical_numbers)
        return lexicographical_numbers

    def _generate_lexical_numbers(
        self, current_number: int, limit: int, result: List[int]
    ):
        # If the current number exceeds the limit, stop recursion
        if current_number > limit:
            return
        # Add the current number to the result
        result.append(current_number)

        # Try to append digits from 0 to 9 to the current number
        for next_digit in range(10):
            next_number = current_number * 10 + next_digit
            # If the next number is within the limit, continue recursion
            if next_number <= limit:
                self._generate_lexical_numbers(next_number, limit, result)
            else:
                break  # No need to continue if next_number exceeds limit
