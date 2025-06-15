class Solution:
    def generateTag(self, caption: str) -> str:
        words = caption.split()
        res = "#"
        firstWord = True
        for w in words:
            first = True
            for char in w:
                if char.isalpha():
                    if firstWord and first:
                        res += char.lower()
                        firstWord = False
                        first = False
                    elif first:
                        res += char.upper()
                        first = False
                    else:
                        res += char.lower()
            if len(res) > 100:
                break
            
        return res[0:100]
            
        
# runtime: O(n)
# spacetime: O(1)
