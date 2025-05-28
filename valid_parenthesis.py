class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in mapping:
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)

                

        return len(stack) == 0  # Stack should be empty if valid

# 🔍 Test cases
sol = Solution()
print(sol.isValid("()[]{}"))      # Expected: True
print(sol.isValid("(]"))          # Expected: False
print(sol.isValid("([{}])"))      # Expected: True
print(sol.isValid("((({{{[[[]]]}}})))"))  # Expected: True
print(sol.isValid("((("))         # Expected: False
