class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            # starting bracket
            if s[i] == "[":
                stack.append(("[", "left"))
                i += 1
            elif s[i] == "]": # take off from the stack until you get a number
                chars = stack.pop()[0]
                while stack and stack[-1][1] == "chars":
                    print(stack)
                    chars = stack.pop()[0] + chars
                left_bracket = stack.pop()
                number = stack.pop()
                print(stack)
                count = int(number[0])
                final_chars = ""
                while count > 0:
                    final_chars += chars
                    count -= 1
                res = final_chars
                while stack and stack[-1][1] == "chars":
                    res = stack.pop()[0] + res
                stack.append((res, "chars"))
                i += 1
            elif s[i].isdigit(): # get the whole number and add to stack
                num = ""
                while s[i].isdigit():
                    num += s[i]
                    i += 1
                stack.append((num, "num"))
            else: # this is alphabet so just get until number or bracket
                chars = ""
                while i < len(s) and not s[i].isdigit() and s[i] != "[" and s[i] != "]":
                    chars += s[i]
                    i += 1
                stack.append((chars, "chars"))
        ans = ""
        print(stack)
        for i in range(len(stack)):
            ans += stack[i][0]
        return ans
            
                


                
        

