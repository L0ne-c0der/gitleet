class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            match char:
                case '(' | '{' | '[':
                    stack.append(char)
                case ')':
                    if not stack or stack.pop() != '(':
                        return False
                case '}':
                    if not stack or stack.pop() != '{':
                        return False
                case ']':
                    if not stack or stack.pop() != '[':
                        return False
                case _: # For any other unexpected characters, though problem constraints usually limit this
                    return False # Or handle as per problem requirements

        return not stack