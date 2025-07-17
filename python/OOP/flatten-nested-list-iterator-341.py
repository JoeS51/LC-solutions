class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        def getNList(nestedList):
            res = []
            if nestedList.isInteger():
                return [nestedList.getInteger()]
            for nlist in nestedList.getList():
                if nlist.isInteger():
                    res.append(nlist.getInteger())
                else:
                    curr_list = getNList(nlist)
                    for i in curr_list:
                        res.append(i)
            return res

        self.l = []
        for n in nestedList:
            curr = getNList(n)
            for i in curr:
                self.l.append(i)
        self.i = 0

    
    def next(self) -> int:
        if self.hasNext():
            # get next
            return self.l.pop(0)
        else:
            return

    def hasNext(self) -> bool:
        if len(self.l) > 0:
            return True
        return False
        
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

