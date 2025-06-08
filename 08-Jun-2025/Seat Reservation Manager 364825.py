# Problem: Seat Reservation Manager - https://leetcode.com/problems/seat-reservation-manager/description/

class SeatManager:

    def __init__(self, n: int):
        self.available = []
        self.next_seat = 1
        

    def reserve(self) -> int:
        if self.available:
            return heapq.heappop(self.available)
        seat = self.next_seat
        self.next_seat += 1
        return seat
        

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.available, seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)