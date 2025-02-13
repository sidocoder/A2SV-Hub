# Problem: Minimum Number of Moves To Seat Everyone - https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
    
        seats.sort()
        students.sort()
        return sum(abs(seats[i] - students[i]) for i in range(len(seats)))
