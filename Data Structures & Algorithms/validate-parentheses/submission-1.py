class Solution:
    def isValid(self, s: str) -> bool:
        size = len(s)

        if size % 2 != 0:
            return False

        stack = []

        for i in range(size):
            c = s[i]

            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False

                top = stack[-1]

                if top == '(' and c == ')':
                    stack.pop()
                elif top == '[' and c == ']':
                    stack.pop()
                elif top == '{' and c == '}':
                    stack.pop()
                else:
                    stack.append(c)
        
        return len(stack) == 0






