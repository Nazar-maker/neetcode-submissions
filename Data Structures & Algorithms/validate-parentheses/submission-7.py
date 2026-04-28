class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)

            else:
                if not stack: return False
                parenthesis = stack.pop()
                if parenthesis == '(' and c != ')': return False
                elif parenthesis == '[' and c != ']': return False
                elif parenthesis == '{' and c != '}': return False

        return True if not stack else False
