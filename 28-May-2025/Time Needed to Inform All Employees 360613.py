# Problem: Time Needed to Inform All Employees - https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        tree = defaultdict(list)
        for i in range(n):
            if manager[i] != -1:
                tree[manager[i]].append(i)

        # DFS function to calculate time
        def dfs(emp_id):
            if emp_id not in tree:  # No subordinates
                return 0
            max_time = 0
            for subordinate in tree[emp_id]:
                max_time = max(max_time, dfs(subordinate))
            return informTime[emp_id] + max_time

        return dfs(headID)
