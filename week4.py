def get_path(node):
    path = []
    current = node
    while current:
        path.append((current.state, current.action))
        current = current.parent
    return path[::-1]

def get_neighbors(state):
    neighbors = []
    empty_index = state.index(0)
    row, col = divmod(empty_index, 3)

    for move in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        new_row, new_col = row + move[0], col + move[1]
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            neighbor_state = list(state)
            neighbor_index = new_row * 3 + new_col
            neighbor_state[empty_index], neighbor_state[neighbor_index] = (
                neighbor_state[neighbor_index],
                neighbor_state[empty_index],
            )
            neighbors.append(tuple(neighbor_state))

    return neighbors

def depth_limited_search(state, goal_state, depth_limit, parent=None, action=None):
    if state == goal_state:
        return True
    elif depth_limit == 0:
        return False
    else:
        for neighbor_state in get_neighbors(state):
            # Pass correct parameters to the recursive call
            result = depth_limited_search(
                neighbor_state, goal_state, depth_limit - 1, state, action
            )
            if result:  # Check the result of the recursive call
                return True
        return False

# Example usage
initial_state = eval(input("src= "))
goal_state = eval(input("target= "))
depth_limit = int(input("Enter the depth limit:"))

result = depth_limited_search(initial_state, goal_state, depth_limit)
print(result)
