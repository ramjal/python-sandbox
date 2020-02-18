class Solution:    
    def isValid(self, s):
        if len(s) == 0:
            return True
        stack = []
        for c in s:
            if len(stack) == 0:
                stack.append(c)
            else:
                peek = stack[-1]
                if peek == "(" and c == ")":
                    stack.pop()
                elif peek == "{" and c == "}":
                    stack.pop()
                elif peek == "[" and c == "]":
                    stack.pop()
                else:
                    stack.append(c)        
        if len(stack) == 0:
            return True
        else:
            return False



# Test Program
s = "()(){(())" 
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))

s = "{([{}])()(([]))[{{}}]}"
# should return True
print(Solution().isValid(s))

s = "{([{}])()(([]))[{{}}]}]"
# should return False
print(Solution().isValid(s))