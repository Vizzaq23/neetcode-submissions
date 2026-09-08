class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {')': '(', ']': '[', '}': '{'}
        for char in s:
            if char in ")]}":
                if not stack:
                    return False
                opener = stack.pop()
                if opener != matching[char]:
                    return False
            else:
                stack.append(char)
        return not stack
