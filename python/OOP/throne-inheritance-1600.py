class ThroneInheritance:

    class Node:
        def __init__(self, name):
            self.name = name
            self.children = []

    def successor(self, root: Node, parent: str, child: str):
        if root.name == parent:
            root.children.append(self.Node(child))
            return

        for n in root.children:
            self.successor(n, parent, child)
        return
    
    def printOrder(self, root: Node, res: list()):
        if not root:
            return
        res.append(root.name)
        for n in root.children:
            self.printOrder(n, res)
        return

    def removeNode(self, root, name):
        if not root:
            return 
        
        for i, n in enumerate(root.children):
            if n.name == name:
                print("tru")
                if n.children:
                    print("if")
                    firstChild = n.children[0]
                    x = len(n.children)
                    for i in range(1, x):
                        firstChild.children.append(n.children[i])
                    root.children[i] = firstChild
                else:
                    print("else")
                    del root.children[i]
                return
            self.removeNode(n, name)
        return
    
        

    def __init__(self, kingName: str):
        self.rootNode = self.Node(kingName)

    def birth(self, parentName: str, childName: str) -> None:
        self.successor(self.rootNode, parentName, childName)
        return
        

    def death(self, name: str) -> None:
        if rootNode.name == name:
            # replace root node with first child and all other children point to this 
            firstChild = rootNode.children[0]
            x = len(rootNode.children)
            for i in range(1, x):
                firstChild.children.append(rootNode.children[i])
            rootNode = firstChild
            
        self.removeNode(self.rootNode, name)

    def getInheritanceOrder(self) -> List[str]:
        res = []
        self.printOrder(self.rootNode, res)
        return res
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()



