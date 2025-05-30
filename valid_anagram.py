class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == 0 and len(t) == 0:
            return True
        
        if len(s) != len(t):
            return False
        char_count = {}
        
        for char in s:
            char_count[char] = char_count.get(char,0)+1
        
        for char in t:
            if char not in char_count or char_count[char] == 0:
                return False
            char_count[char] -= 1

        return True
        

# Example usage (for your local testing):
sol = Solution()
print(sol.isAnagram("anagram", "nagaram")) # Expected: True
print(sol.isAnagram("rat", "car"))         # Expected: False
print(sol.isAnagram("", ""))               # Expected: True (edge case)
print(sol.isAnagram("a", "a"))             # Expected: True
print(sol.isAnagram("ab", "a"))            # Expected: False