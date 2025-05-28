from collections import deque

class Solution:
    def firstNegativeInWindow(self, nums: list[int], k: int) -> list[int]:
        result = []
        neg_queue = deque()

        for i in range(len(nums)):
            # Add current element if it is negative
            if nums[i] < 0:
                neg_queue.append(i)

            # Remove elements that are out of the current window
            if neg_queue and neg_queue[0] < i - k + 1:
                neg_queue.popleft()

            # Record result when window hits size k
            if i >= k - 1:
                if neg_queue:
                    result.append(nums[neg_queue[0]])
                else:
                    result.append(0)
        
        return result

# 🔍 Test it
sol = Solution()
print(sol.firstNegativeInWindow([12, -1, -7, 8, 15, 30, 16, 28], 3))  # Expected: [-1, -1, -7, 0, 0, 0]
