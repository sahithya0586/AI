from collections import deque

# Function to generate next valid moves from a state
def get_neighbors(state):
    neighbors = []
    state = list(state)
    idx = state.index('_')

    def swap(i, j):
        new_state = state[:]
        new_state[i], new_state[j] = new_state[j], new_state[i]
        return ''.join(new_state)

    # Right-moving rabbits (R) to the right
    if idx > 0 and state[idx - 1] == 'R':
        neighbors.append(swap(idx, idx - 1))
    if idx > 1 and state[idx - 2] == 'R':
        neighbors.append(swap(idx, idx - 2))

    # Left-moving rabbits (L) to the left
    if idx < len(state) - 1 and state[idx + 1] == 'L':
        neighbors.append(swap(idx, idx + 1))
    if idx < len(state) - 2 and state[idx + 2] == 'L':
        neighbors.append(swap(idx, idx + 2))

    return neighbors

# BFS to find shortest path
def bfs(start, goal):
    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None

# DFS to find any path (not necessarily shortest)
def dfs(start, goal):
    stack = [(start, [start])]
    visited = set()

    while stack:
        state, path = stack.pop()
        if state == goal:
            return path

        if state not in visited:
            visited.add(state)
            for neighbor in get_neighbors(state):
                stack.append((neighbor, path + [neighbor]))
    return None

# Driver code
if __name__ == "__main__":
    start_state = "RRR_LLL"
    goal_state = "LLL_RRR"

    print(" BFS Path (Shortest):")
    bfs_path = bfs(start_state, goal_state)
    for step in bfs_path:
        print(step)

    print("\n DFS Path :")
    dfs_path = dfs(start_state, goal_state)
    for step in dfs_path:
        print(step)

