class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pair = {
            ']':'[',
            '}':'{',
            ')':'('
        }

        for i in range(len(s)):
            if s[i] in "[{(":
                stack.append(s[i])
            else:
                if not stack:
                    return False

                if stack[-1] != pair[s[i]]:
                    return False
                stack.pop()
        
        return True if len(stack) == 0 else False