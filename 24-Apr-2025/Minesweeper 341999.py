# Problem: Minesweeper - https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        rows = len(board)
        cols = len(board[0])
        a,b = click[0], click[1]
        if board[a][b] == 'M':
            board[a][b] = "X"
            return board
        else:
            queue = deque([(a,b)])
            directions = [(-1,0),(0,-1),(0,1),(1,0),(-1,-1),(1,1),(-1,1),(1,-1)]

            visited = set()

            while queue:                
                a,b = queue.popleft()
                if (a, b) in visited:
                    continue
                else:
                    visited.add((a, b))

                count = 0
                for r,c in directions:
                    nr,nc = a + r, b + c
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if board[nr][nc] == "M":
                            count +=1 
                if count > 0:
                    board[a][b] = str(count)
                else:
                    board[a][b] = "B"
                    for r,c in directions:
                        nr,nc = r + a,c+ b
                        if 0 <= nr < rows and 0 <= nc < cols:

                            queue.append((nr,nc))
                    
            return board 


        