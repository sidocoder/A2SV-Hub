# Problem: D - Life Across the Stars - https://codeforces.com/gym/591928/problem/D

from collections import defaultdict

n = int(input())
events = defaultdict(int)

# Mark birth and death events
for _ in range(n):
    birth, death = map(int, input().split())
    events[birth] += 1
    events[death] -= 1  # Death marks the end of life

# Sort event years
years = sorted(events.keys())

# Sweep through the years
max_people = 0
year = 0
current_population = 0

for y in years:
    current_population += events[y]
    if current_population > max_people:
        max_people = current_population
        year = y  # Pick the smallest year in case of ties

print(year, max_people)