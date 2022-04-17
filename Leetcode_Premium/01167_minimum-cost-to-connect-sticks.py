import heapq
class Solution:
    def minimum_cost(self, sticks: List[int]) -> int:
        # write your code here
        heapq.heapify(sticks)
        cost = 0
        while len(sticks) > 1:
            c = heapq.heappop(sticks)
            c += heapq.heappop(sticks)
            cost += c
            heapq.heappush(sticks, c)
        return cost
