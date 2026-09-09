class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            stack_size = len(stack)
            if stack_size == 0:
                stack.append(char)
            else:
                if ((stack[stack_size-1] =='(' and char == ')')
                    or (stack[stack_size-1] =='{' and char == '}')
                        or (stack[stack_size-1] =='[' and char == ']')):
                        stack.pop()
                else:
                    stack.append(char)
        if len(stack) > 0:
            return False
        return True
