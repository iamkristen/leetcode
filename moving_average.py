from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.sum = 0

    def next(self, val: int) -> float:
        if len(self.queue) == self.size:
            removed = self.queue.popleft()
            self.sum -= removed
        self.queue.append(val)
        self.sum += val
        return self.sum/len(self.queue) 
        # Step 1: Add the new value to the queue
        # Step 2: If queue is too big, remove the oldest value
        # Step 3: Update the running sum
        # Step 4: Return the average (sum / len(queue))


# 🔍 Test it
m = MovingAverage(3)
print(m.next(1))    # → 1.0
print(m.next(10))   # → 5.5
print(m.next(3))    # → 4.67
print(m.next(5))    # → 6.0
