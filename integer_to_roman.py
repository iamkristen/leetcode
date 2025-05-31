class Solution:
    def intToRoman(self, num: int) -> str:
        roman_map = {
            1: "I", 4: "IV", 5: "V", 9: "IX",
            10: "X", 40: "XL", 50: "L", 90: "XC",
            100: "C", 400: "CD", 500: "D", 900: "CM",
            1000: "M"
        }

        values = sorted(roman_map.keys(), reverse=True)
        roman = ""

        for v in values:
            while num >= v:
                roman += roman_map[v]
                num -= v

        return roman

# ✅ Test
sol = Solution()
print(sol.intToRoman(3749))