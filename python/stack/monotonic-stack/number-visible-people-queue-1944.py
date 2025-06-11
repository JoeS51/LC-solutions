class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = []
        res = [0] * len(heights)
        i = len(heights) - 1
        for x in reversed(heights):
            # print(stack)
            # print("-------")
            if not stack:
                res[i] = 0
                stack.append(x)
            else:
                top = stack[-1]
                if top > x:
                    stack.append(x)
                    res[i] = 1
                else:
                    cnt = 0
                    while top and top < x:
                        stack.pop()
                        cnt += 1
                        if not stack:
                            break
                        top = stack[-1]
                    if stack:
                        cnt += 1
                    stack.append(x)
                    res[i] = cnt
            i -= 1
        return res

# runtime: O(n)
# spacetime: O(n)
        

