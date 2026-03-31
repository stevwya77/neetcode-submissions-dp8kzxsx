class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenDict = {")":"(", "}": "{", "]":"["}

        for char in s:
            if char in parenDict:
                if stack and stack[-1] == parenDict[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False