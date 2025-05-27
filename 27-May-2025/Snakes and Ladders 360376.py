# Problem: Snakes and Ladders - https://leetcode.com/problems/snakes-and-ladders/

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        
        def get_board_mapping():
            mapping = [-1] * (n * n + 1)
            idx = 1
            left_to_right = True
            for r in range(n - 1, -1, -1):
                row = range(n) if left_to_right else range(n - 1, -1, -1)
                for c in row:
                    mapping[idx] = board[r][c]
                    idx += 1
                left_to_right = not left_to_right
            return mapping

        flat_board = get_board_mapping()
        visited = set()
        queue = deque([(1, 0)])  

        while queue:
            pos, moves = queue.popleft()
            for i in range(1, 7):  
                next_pos = pos + i
                if next_pos > n * n:
                    continue
                if flat_board[next_pos] != -1:
                    next_pos = flat_board[next_pos]
                if next_pos == n * n:
                    return moves + 1
                if next_pos not in visited:
                    visited.add(next_pos)
                    queue.append((next_pos, moves + 1))

        return -1
            