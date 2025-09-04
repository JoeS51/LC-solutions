class Tree:
    def __init__(self, symbol: str, last: bool):
        self.children = set()
        self.symbol = symbol
        self.last = last

    def add_child(self, name):
        self.children.add(name)

    def contains_child(self, name):
        for c in self.children:
            if c.symbol == name:
                return True
        return False

    def get_child(self, name):
        for c in self.children:
            if c.symbol == name:
                return c

    def getLast(self):
        return self.last

class Solution:
    def test(input: list[str]):
        tree = Tree("", False)
        curr = tree
        for path in input:
            dir = path.split("/")
            curr = tree
            for i in range(1, len(dir)):
                curr_dir = dir[i]
                last = (i == len(dir) - 1)
                new_tree = Tree(curr_dir, last)
                if curr.contains_child(curr_dir):
                    curr = curr.get_child(curr_dir)
                else:
                    curr.add_child(new_tree)
                    curr = new_tree

        # traverse tree
        def dfs(curr, offset):
            if curr.getLast():
                print(offset + curr.symbol)
                return
            print(offset + curr.symbol)
            for child in curr.children:
                dfs(child, offset + "  ")

        dfs(tree, "")

if __name__ == "__main__":
    example1 = ["/webapp/assets/html/a.html", "/webapp/assets/html/b.html", "/webapp/assets/js/c.js", "/webapp/index.html"]
    Solution.test(example1)
