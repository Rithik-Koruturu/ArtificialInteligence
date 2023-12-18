import random

def print_puzzle(state):
    for i in range(0, 9, 3):
        print(state[i], state[i + 1], state[i + 2])
    print()

def find_empty_space(state):
    return state.index(0)

def is_solved(state, goal_state):
    return state == goal_state

def make_move(state, move):
    empty_index = find_empty_space(state)
    if move == 'up':
        if empty_index not in (0, 1, 2):
            state[empty_index], state[empty_index - 3] = state[empty_index - 3], state[empty_index]
    elif move == 'down':
        if empty_index not in (6, 7, 8):
            state[empty_index], state[empty_index + 3] = state[empty_index + 3], state[empty_index]
    elif move == 'left':
        if empty_index not in (0, 3, 6):
            state[empty_index], state[empty_index - 1] = state[empty_index - 1], state[empty_index]
    elif move == 'right':
        if empty_index not in (2, 5, 8):
            state[empty_index], state[empty_index + 1] = state[empty_index + 1], state[empty_index]

goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

# Input the scrambled initial state
print("Enter the initial state of the puzzle with spaces between each digit:")
initial_state = list(map(int, input().split()))

def solve_puzzle(initial_state, goal_state):
    # Implement an automated puzzle-solving algorithm here
    # You can use A* search, BFS, DFS, or other search algorithms to find a solution
    # Modify the 'initial_state' list to reach the 'goal_state'

    # For demonstration purposes, we will use a simple random shuffle
    while not is_solved(initial_state, goal_state):
        possible_moves = ['up', 'down', 'left', 'right']
        move = random.choice(possible_moves)
        make_move(initial_state, move)
        print_puzzle(initial_state)

    print("Puzzle solved!")

# Solve the puzzle
solve_puzzle(initial_state, goal_state)
