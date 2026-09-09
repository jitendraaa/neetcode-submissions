class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            stack_size = len(stack)
            if stack_size == 0:
                stack.append(int(token))
            else:
                if token == '+':
                    second = stack.pop()
                    first = stack.pop()
                    temp = first + second
                    stack.append(temp)
                elif token == '-':
                    second = stack.pop()
                    first = stack.pop()
                    temp = first - second
                    stack.append(temp)
                elif token == '*':
                    second = stack.pop()
                    first = stack.pop()
                    temp = first * second
                    stack.append(temp)
                elif token == '/':
                    second = stack.pop()
                    first = stack.pop()
                    temp = int(first / second)
                    stack.append(temp)
                else:
                    stack.append(int(token))
        return stack.pop()