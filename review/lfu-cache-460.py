# - get and put need to be O(1) that indicates that it can't be using a heap since that's logn
# - ds that are O(1): hashmap, treemap, array if just indexed
#
# what about buckets? 
# [1, 2, 3, 4, ... 2 * 10^5] -> number of times accessed
# [[], [k3, k1, k2], [k4], []] - linked list with hashmap pointing to each key, value in the linked list for O(1) access
# OR ordered dict??
#        ^                 pointer
#
# curr = 2
# ptr = 0               doesnt matter until curr == capacity
# also just maintain a hashmap for the get
# [1, 2, 3, 4, 5, 6, 7, 8] -> number of times accessed
# [[1, 2]]
#
# 
#
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.ptr = 1
        self.arr = []
        self.m = {}
        self.freqs = {}
        for i in range(0, 100000):
            self.arr.append(OrderedDict())
        

    def get(self, key: int) -> int:
        if key in self.m:
            # and we need to bump up the freqs
            idx = self.freqs[key]
            # old map you're removing from
            prev_dict = self.arr[idx]
            new_dict = self.arr[idx + 1]
            prev_dict.pop(key)
            new_dict[key] = 1
            self.freqs[key] += 1
            # how do you know to increase the ptr?
            if not prev_dict and self.ptr == idx:
                self.ptr += 1
            return self.m[key]
        return -1
        
    # TODO MAke sure the ptr is correct
    def put(self, key: int, value: int) -> None:
        if self.size < self.capacity or key in self.freqs:
            if key in self.m:
                idx = self.freqs[key]
                # old map you're removing from
                prev_dict = self.arr[idx]
                new_dict = self.arr[idx + 1]
                prev_dict.pop(key)
                new_dict[key] = value
                self.freqs[key] += 1
                # how do you know to increase the ptr?
                if not prev_dict and self.ptr == idx:
                    self.ptr += 1
            else:
                self.size += 1
                # adding a new entry to the ordered dict
                self.arr[1][key] = value
                self.freqs[key] = 1
                self.ptr = 1
        else:
            # we have reached capacity so we need to evict something. we can look at ptr for that
            dict_to_remove_from = self.arr[self.ptr]
            removed_key, removed_value = dict_to_remove_from.popitem(last=False) # pop the item inserted first since that is the LRU item
            self.freqs.pop(removed_key)
            self.m.pop(removed_key)
            self.arr[1][key] = value
            self.freqs[key] = 1
            self.ptr = 1
        self.m[key] = value
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

