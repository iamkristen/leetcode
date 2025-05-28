class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_str = ""
        num = 0

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char) 
            elif char == '[':
                stack.append((current_str, num))
                print(stack)
                current_str = ""
                num = 0
            elif char == ']':
                prev_str, repeat = stack.pop()
                current_str = prev_str + (current_str * repeat)
            else:
                current_str += char

        return current_str

sol = Solution()
print(sol.decodeString("3[a2[c]]"))       # Output: accaccacc
print(sol.decodeString("2[abc]3[cd]e\f"))  # Output: abcabccdcdcdef
print(sol.decodeString("3[a]2[bc]"))