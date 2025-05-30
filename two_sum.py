class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Your code goes here
        nums_map = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in nums_map:
                return [nums_map[compliment],i]
            else:
                nums_map[nums[i]] = i
        return []


# Example usage (for your local testing):
sol = Solution()
print(sol.twoSum([2,7,11,15], 9)) # Expected: [0, 1]
print(sol.twoSum([3,2,4], 6))     # Expected: [1, 2]
print(sol.twoSum([3,3], 6))       # Expected: [0, 1]