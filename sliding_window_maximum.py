from collections import deque

class SlidingWindowMax:
    def __init__(self, k: int):
        self.k = k
        self.deque = deque()
        self.result = []

    def maxSlidingWindow(self, nums: list[int]) -> list[int]:
        
        for i in range(len(nums)):
            if self.deque and self.deque[0] < i - self.k+1:
                self.deque.popleft()
            
            while self.deque and nums[self.deque[-1]] < nums[i]:
                self.deque.pop()
            
            self.deque.append(i)

            if i >= self.k-1:
                self.result.append(nums[self.deque[0]])
            
        return self.result

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
swm = SlidingWindowMax(k)
output = swm.maxSlidingWindow(nums)
print(output)