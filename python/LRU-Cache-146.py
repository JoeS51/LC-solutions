class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.first_node = None
        self.last_node = None
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        if len(self.cache) == 1:
            return self.cache[key].value
        
        curr_node = self.cache[key]
        
        if curr_node == self.first_node:
            return self.cache[key].value
        elif curr_node == self.last_node:
            second_to_last = curr_node.prev
            # should never be None
            second_to_last.next = None
            self.last_node = second_to_last
        else:
            prev_node = curr_node.prev
            next_node = curr_node.next
            prev_node.next = next_node
            next_node.prev = prev_node
        
        curr_first_node = self.first_node
        curr_node.next = curr_first_node
        curr_first_node.prev = curr_node
        self.first_node = curr_node
        return self.cache[key].value

    def put(self, key: int, value: int) -> None:
        # if key is already in cache just bring it to the front and replace old val
        if key in self.cache:
            self.get(key)
            self.cache[key].value = value
            return
        new_node = self.Node(key, value, None, None) 

        if len(self.cache) == 0:
            self.first_node = new_node
            self.last_node = new_node
        
        if self.capacity == 1:
            old_node = self.first_node
            self.first_node = new_node
            self.last_node = new_node
            self.cache[key] = new_node
            if len(self.cache) == 2:
                del self.cache[old_node.key]
            return

        if len(self.cache) == self.capacity:
            second_to_last = self.last_node.prev
            del self.cache[self.last_node.key]
            second_to_last.next = None
            self.last_node = second_to_last
        
        curr_first_node = self.first_node
        curr_first_node.prev = new_node
        new_node.next = curr_first_node
        self.first_node = new_node
        self.cache[new_node.key] = new_node

    class Node:
        def __init__(self, key: int, value: int, prev, next):
            self.key = key
            self.value = value
            self.prev = prev
            self.next = next
        

# This problem was suprisingly more difficult than I thought. There are a lot of edge cases to think about for if the capacity is 1 or 2, so make sure to think about them before typing


