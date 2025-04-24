# Problem: Flood Fill - https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        queue = deque()
        starting = image[sr][sc]
        rows = len(image)
        cols = len(image[0])

        if starting == color:
            return image
        else:
            queue.append((sr, sc))
            image[sr][sc] = color
            
            
            directions = [(0,1),(1,0),(-1,0),(0,-1)]
            
            while queue:
                r,c = queue.popleft()
                for a,b in directions:
                    nr, nc = a + r, b + c
                    if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == starting:
                        image[nr][nc] = color
                        queue.append((nr,nc))
            return image



        