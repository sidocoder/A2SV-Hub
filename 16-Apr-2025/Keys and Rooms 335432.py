# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # visited = [0]
       
        # for num in rooms:
        #     index = rooms.index(num)
        #     for item in num:
        #         if item != index and item not in visited:
        #             visited.append(item)
        
        # return len(visited) == len(rooms)
        graph = defaultdict(list)

        for num in rooms:
            index = rooms.index(num)
            for item in num:
                graph[index].append(item)
        visited = set([0])
        queue = deque([0])

        while queue:
            
            room = queue.popleft()
        
            for key in graph[room]:
                if key not in visited:
                    visited.add(key)
                    queue.append(key)
        return len(visited) == len(rooms)

        




