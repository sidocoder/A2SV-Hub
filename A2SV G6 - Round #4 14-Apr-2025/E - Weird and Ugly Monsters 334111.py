# Problem: E - Weird and Ugly Monsters - https://codeforces.com/gym/590053/problem/E

class ListNode:
    def __init__(self, index, ugliness):
        # Initialize a new monster node with an index and ugliness score.
        self.index = index
        self.ugliness = ugliness
        self.next = None
        self.prev = None


def merge_monsters(node, monster_map, count):
    # Try to merge the node with its adjacent neighbors (left and right) as long as they have the same ugliness score.
    while True:
        merged = False

        # Merge with the left neighbor if they have the same ugliness
        if node.prev != node and node.ugliness == node.prev.ugliness:
            left = node.prev
            if node.index > left.index:
                # Adjust the pointers to remove 'node' and merge with the left neighbor
                left.next = node.next
                node.next.prev = left
                left.ugliness *= 2
                count[0] -= 1  # Decrease the count of monsters after merging
                node = left  # Move 'node' to 'left' as it is now the active node
            else:
                # Adjust the pointers to remove 'left' and merge with 'node'
                node.prev = left.prev
                left.prev.next = node
                node.ugliness *= 2
                count[0] -= 1  # Decrease the count of monsters after merging
            merged = True

        # Merge with the right neighbor if they have the same ugliness
        elif node.next != node and node.ugliness == node.next.ugliness:
            right = node.next
            if node.index > right.index:
                # Adjust the pointers to remove 'node' and merge with the right neighbor
                node.prev.next = right
                right.prev = node.prev
                right.ugliness *= 2
                count[0] -= 1  # Decrease the count of monsters after merging
                node = right  # Move 'node' to 'right' as it is now the active node
            else:
                # Adjust the pointers to remove 'right' and merge with 'node'
                right.next.prev = node
                node.next = right.next
                node.ugliness *= 2
                count[0] -= 1  # Decrease the count of monsters after merging
            merged = True

        # Exit the loop if no merges happened
        if not merged:
            break


def solve():
    # Solve the problem for a single test case
    num_insertions, initial_ugliness = map(int, input().split())

    # Count is an array of 1 value because it is passed to the merge
    # function and we need to modify the value in that function
    count = [1]  # Initialize count to 1 since we have 1 monster initially

    head = ListNode(1, initial_ugliness)
    head.next = head  # Make the list circular by linking the head to itself
    head.prev = head
    monster_map = {1: head}  # Map to track the monsters by their index

    indices = list(map(int, input().split()))
    ugliness_values = list(map(int, input().split()))
    next_index = 2  # Start from the next available index for the new monsters
    results = []

    for i in range(num_insertions):
        monster_index, ugliness_score = indices[i], ugliness_values[i]
        monster = monster_map[monster_index]

        # Create and insert the new monster into the linked list
        new_monster = ListNode(next_index, ugliness_score)
        next_index += 1

        # Adjust the pointers to add the new monster
        new_monster.next = monster.next
        new_monster.prev = monster
        monster.next.prev = new_monster
        monster.next = new_monster

        monster_map[new_monster.index] = new_monster  # Add the new monster to the map
        count[0] += 1  # Increase the count after adding a new monster

        # Perform merges after insertion
        merge_monsters(new_monster, monster_map, count)

        # Store the current number of monsters after the insertion and merges
        results.append(count[0])

    print(*results)


t = int(input())
for _ in range(t):
    solve()