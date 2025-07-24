from collections import deque
from itertools import combinations

# Time mapping for each person
times = {
    "A": 5,
    "M": 10,
    "GM": 20,
    "GF": 25
}

# BFS Search
def bfs():
    initial = (frozenset(times.keys()), frozenset(), 'left', 0, [])  # (left, right, umbrella, time, path)
    queue = deque([initial])
    visited = set()

    while queue:
        left, right, side, current_time, path = queue.popleft()
        
        # Check goal
        if len(left) == 0 and current_time <= 60:
            return path + [("Final Time", current_time)]
        
        state_key = (left, side, current_time)
        if state_key in visited:
            continue
        visited.add(state_key)

        if side == 'left':
            movers = combinations(left, 2) if len(left) > 1 else [(p,) for p in left]
            for pair in movers:
                pair = tuple(pair)
                time_taken = max(times[p] for p in pair)
                new_left = set(left) - set(pair)
                new_right = set(right) | set(pair)
                new_time = current_time + time_taken
                if new_time <= 60:
                    queue.append((frozenset(new_left), frozenset(new_right), 'right', new_time, path + [("→", pair, time_taken)]))
        else:  # umbrella on right, one must return
            for p in right:
                time_taken = times[p]
                new_left = set(left) | {p}
                new_right = set(right) - {p}
                new_time = current_time + time_taken
                if new_time <= 60:
                    queue.append((frozenset(new_left), frozenset(new_right), 'left', new_time, path + [("←", (p,), time_taken)]))
    return None

# DFS Search
def dfs():
    initial = (frozenset(times.keys()), frozenset(), 'left', 0, [])
    stack = [initial]
    visited = set()

    while stack:
        left, right, side, current_time, path = stack.pop()

        if len(left) == 0 and current_time <= 60:
            return path + [("Final Time", current_time)]

        state_key = (left, side, current_time)
        if state_key in visited:
            continue
        visited.add(state_key)

        if side == 'left':
            movers = combinations(left, 2) if len(left) > 1 else [(p,) for p in left]
            for pair in movers:
                pair = tuple(pair)
                time_taken = max(times[p] for p in pair)
                new_left = set(left) - set(pair)
                new_right = set(right) | set(pair)
                new_time = current_time + time_taken
                if new_time <= 60:
                    stack.append((frozenset(new_left), frozenset(new_right), 'right', new_time, path + [("→", pair, time_taken)]))
        else:
            for p in right:
                time_taken = times[p]
                new_left = set(left) | {p}
                new_right = set(right) - {p}
                new_time = current_time + time_taken
                if new_time <= 60:
                    stack.append((frozenset(new_left), frozenset(new_right), 'left', new_time, path + [("←", (p,), time_taken)]))
    return None

# Driver
if __name__ == "__main__":
    print(" BFS Solution:")
    bfs_result = bfs()
    for step in bfs_result:
        print(step)

    print("\n DFS Solution:")
    dfs_result = dfs()
    for step in dfs_result:
        print(step)

