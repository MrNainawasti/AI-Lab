from queue import PriorityQueue


GOAL_STATE = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]
            

def calculate_heuristic(state):
    h = 0
    for i in range(3):
        for j in range(3):
            element = state[i][j]
            if element != 0:
                target_x = (element-1)//3
                target_y = (element-1)%3
                h_of_n += abs(i - target_x) + abs(j - target_y)             
    return h


def find_blank_tile(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
            

def get_neighbours(state):
    neighbours = []
    x, y = find_blank_tile(state)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for x_mov, y_mov in moves:
        new_x = x + x_mov
        new_y = y + y_mov
        if 0 <= new_x < 3 and 0 <= new_y < 3:
           new_state = [row[:] for row in state]
           new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
           neighbours.append(new_state)
    return neighbours
           
    
def a_star(start_state):
    open_list = PriorityQueue()
    open_list.put((0, start_state, 0, None))  # (f(n), state, g(n), parent)
    closed_set = set()
    parents = {} 
    
    while not open_list.empty():
        _, current_state, g, parent = open_list.get()
        
        # Goal check
        if current_state == GOAL_STATE:
            path = []
            while current_state:
                path.append(current_state)
                current_state = parents.get(tuple(map(tuple, current_state)))
            return path[::-1]  # Return path in correct order
        
        closed_set.add(tuple(map(tuple, current_state)))
        parents[tuple(map(tuple, current_state))] = parent
        
        # Expand neighbors
        for neighbor in get_neighbours(current_state):
            if tuple(map(tuple, neighbor)) in closed_set:
                continue
            h = calculate_heuristic(neighbor)
            f = g + 1 + h
            open_list.put((f, neighbor, g + 1, current_state))
    
    return None  # No solution found


def print_state(state):
    for row in state:
        print(row)
    print()

start_state = [[1, 2, 3],
               [4, 0, 5],
               [7, 8, 6]]

solution_path = a_star(start_state)
if solution_path:
    print("Solution found in {} moves:\n".format(len(solution_path) - 1))
    for state in solution_path:
        print_state(state)
else:
    print("No solution found!")






