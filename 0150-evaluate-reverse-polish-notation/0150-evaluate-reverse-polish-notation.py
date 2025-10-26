class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def is_integer(s):
            try:
                int(s)
                return True
            except ValueError:
                return False

        stack = []

        for t in tokens:
            if is_integer(t):
                stack.append(int(t))
                continue

            n1 = stack.pop()
            n2 = stack.pop()

        #note that we need to do n2 - n1, because LIFO

            match t:
                case '+':
                    res = n2 + n1
                case '-':
                    res = n2 - n1
                case '*':
                    res = n2 * n1
                case '/':
                    res = int(n2 / n1)
                case _:
                    return

            stack.append(res)

        return stack.pop() if stack else 0

