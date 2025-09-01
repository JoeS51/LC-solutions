class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        m = defaultdict(int)
        for i in s:
            m[i] += 1
        res = []
        curr_count = 0
        curr_chars = set()
        for char in s:
            if char in curr_chars or m[char] == 1:
                m[char] -= 1
                if m[char] == 0:
                    if char in curr_chars:
                        curr_chars.remove(char)
            else:
                curr_chars.add(char)
                m[char] -= 1
            if len(curr_chars) == 0:
                res.append(curr_count+1)
                curr_count = 0
            else:
                curr_count += 1
                    
        return res
            
        

