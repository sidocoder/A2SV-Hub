# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [(et, pt, i) for i, (et, pt) in enumerate(tasks)]
        tasks.sort()  

        n = len(tasks)
        result = []
        time = 0
        i = 0
        heap = []

        while len(result) < n:
            while i < n and tasks[i][0] <= time:
                enqueue_time, process_time, index = tasks[i]
                heapq.heappush(heap, (process_time, index))
                i += 1

            if heap:
                process_time, index = heapq.heappop(heap)
                time += process_time
                result.append(index)
            else:
                time = tasks[i][0]

        return result
