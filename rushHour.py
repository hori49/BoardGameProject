import copy

# Node class stores current board, index of previous path, f(n), and g(n)
class Node():
    def __init__(self, board, prev_state, f_n, g_n):
        self.board = board # current board
        self.prev_state = prev_state # index of previous path
        self.f_n = f_n # f(n) -> h(n) + g(n)
        self.g_n = g_n # g(n) -> actual distance

    def goal_state(self):
        if (self.board[2][5] == 'X'): # check whether the current state reached the goal state
            return True
        else:
            return False

# Print a state
# argument(s) : one state for printing out
# return : None
def print_state(state):
    for i in state:
        print (i)

# Check a new state exists in previous states
# argument(s) : the list of states, a new state
# return : True if the state has already existed False if not
def search_nodes(lst, new_state):
    for state in lst:
        if state.board == new_state.board:
            return True
    return False

# Swap two elements (a and b) in a list
# This function is used for swapping two elements horizontally
# argument(s) : a list for swapping, two column numbers for swapping
# return : swapped list
def swap_horizontal(lst, a, b):
    lst = list(lst)
    lst[a], lst[b] = lst[b], lst[a]
    return ''.join(lst)

# Swap two elements ([row1][col1] and [row2][col2]) in two lists
# This function is used for swapping two elements vertically
# argument(s) : two lists for swapping, column number for swapping
# return : swaped list
def swap_vertical(lst1, lst2, col):
    lst1 = list(lst1)
    lst2 = list(lst2)
    lst1[col], lst2[col] = lst2[col], lst1[col]
    return (''.join(lst1), ''.join(lst2))

# Move a vehicle one square upward
# argument(s) : the current game board state, row number of the current game board, column number of the current game board
# return : the game board state moved one step from the given state (if possible)
def move_up(curr_board, row, col):
    curr_state = copy.deepcopy(curr_board)
    is_truck = False

    if (row == 0 or row == 5):
        return None
    if (curr_state[row][col] == '-'):
        return None
    if (curr_state[row][col] != curr_state[row+1][col] or curr_state[row-1][col] != '-'):
        return None
    if (0 < row and row < 4):
        if (curr_state[row][col] == curr_state[row+2][col]):
            is_truck = True

    # Swap two element
    if (is_truck):
        tmp1, tmp2 = swap_vertical(curr_state[row-1], curr_state[row+2], col)
        curr_state[row-1] = tmp1
        curr_state[row+2] = tmp2
    else:
        tmp1, tmp2 = swap_vertical(curr_state[row-1], curr_state[row+1], col)
        curr_state[row-1] = tmp1
        curr_state[row+1] = tmp2

    return curr_state

# Move a vehicle one square rightward
# argument(s) : the current game board state, row number of the current game board, column number of the current game board
# return : the game board state moved one step from the given state (if possible)
def move_right(curr_board, row, col):
    curr_state = copy.deepcopy(curr_board)
    is_truck = False

    if (col == 0 or col == 5):
        return None
    if (curr_state[row][col] == '-'):
        return None
    if ((curr_state[row][col] != curr_state[row][col-1]) or (curr_state[row][col+1] != '-')):
        return None
    if (1 < col and col < 5):
        if (curr_state[row][col] == curr_state[row][col-2]):
            is_truck = True

    if (is_truck):
        tmp = swap_horizontal(curr_state[row], col+1, col-2)
        curr_state[row] = tmp
    else:
        tmp = swap_horizontal(curr_state[row], col+1, col-1)
        curr_state[row] = tmp

    return curr_state

# Move a vehicle one square downward
# argument(s) : the current game board state, row number of the current game board, column number of the current game board
# return : the game board state moved one step from the given state (if possible)
def move_down(curr_board, row, col):
    curr_state = copy.deepcopy(curr_board)
    is_truck = False

    if (row == 0 or row == 5):
        return None
    if (curr_state[row][col] == '-'):
        return None
    if (curr_state[row][col] != curr_state[row-1][col] or curr_state[row+1][col] != '-'):
        return None
    if (1 < row and row < 5):
        if (curr_state[row][col] == curr_state[row-2][col]):
            is_truck = True

    # Swap two element
    if (is_truck):
        tmp1, tmp2 = swap_vertical(curr_state[row+1], curr_state[row-2], col)
        curr_state[row+1] = tmp1
        curr_state[row-2] = tmp2
    else:
        tmp1, tmp2 = swap_vertical(curr_state[row+1], curr_state[row-1], col)
        curr_state[row+1] = tmp1
        curr_state[row-1] = tmp2

    return curr_state

# Move a vehicle one square leftward
# argument(s) : the current game board state, row number of the current game board, column number of the current game board
# return : the game board state moved one step from the given state (if possible)
def move_left(curr_board, row, col):
    curr_state = copy.deepcopy(curr_board)
    is_truck = False

    if (col == 0 or col == 5):
        return None
    if (curr_state[row][col] == '-'):
        return None
    if (curr_state[row][col] != curr_state[row][col+1] or curr_state[row][col-1] != '-'):
        return None
    if (0 < col and col < 4):
        if (curr_state[row][col] == curr_state[row][col+2]):
            is_truck = True

    if (is_truck):
        tmp = swap_horizontal(curr_state[row], col-1, col+2)
        curr_state[row] = tmp
    else:
        tmp = swap_horizontal(curr_state[row], col-1, col+1)
        curr_state[row] = tmp

    return curr_state

# Create a new node
# argument(s) : the new game board state, heuristic (0 or else), the number of actual paths, the previous game board state
# return : new node
def create_node(new_states, heuristic, g_n, prev_state):
    f_n = get_f_n(heuristic, new_states, g_n)
    return_state = Node(new_states, prev_state, f_n, g_n)
    return return_state

# Send the sort order (ordered by f(n))
# argument(s) : the list of unexplored nodes (unsorted)
# return : the list of unexplored nodes (sorted by f(n))
def sort_by_f(board):
    return board.f_n

# Generates new nodes
# argument(s) : the current game board state, heuristic (0 or else), the number of actual paths
# return : the list of states (possible next step)
def generate_new_states(curr_state, heuristic, g_n):
    new_states = []
    new_states_list = []
    for row in range(0, 6):
        for col in range(0, 6):
            tmp = move_up(curr_state.board, row, col)
            if (tmp != None):
                new_states.append(tmp)
            tmp = move_right(curr_state.board, row, col)
            if (tmp != None):
                new_states.append(tmp)
            tmp = move_down(curr_state.board, row, col)
            if (tmp != None):
                new_states.append(tmp)
            tmp = move_left(curr_state.board, row, col)
            if (tmp != None):
                new_states.append(tmp)

    for i in range(len(new_states)):
        new_states_list.append(create_node(new_states[i], heuristic, g_n, curr_state))

    return new_states_list

# First heuristic --> blocking heuristic
# "blocking" means zero for the goal state, or one plus the number of cars or trucks blocking the path to the exit for all other states.
# h(n) returns zero for the goal state, or one plus the number of cars or trucks blocking the path to the exit for all other states.
# argument(s) : the current game board state
# return : h(n) obtained by blocking
def blocking_heuristic(curr_state):
    if curr_state[2][5] == 'X':
        return 0 # current state is the goal state
    num_blocking_vehicle = 0
    for i in range(0, 6)[::-1]:
        if curr_state[2][i] == 'X':
            return num_blocking_vehicle + 1
        elif curr_state[2][i] != '-':
            num_blocking_vehicle += 1

# Second heuristic (my heuristic) --> h(n) = blocking() + distance(from the car X to the exit)
# "blocking" means zero for the goal state, or one plus the number of cars or trucks blocking the path to the exit for all other states.
# argument(s) : the current game board state
# return : h(n) obtained by blocking + distance(from the car X to the exit) 
def my_heuristic(curr_state):
    if curr_state[2][5] == 'X':
        return 0 # current state is the goal state
    h_n = 0
    for i in range(0, 6)[::-1]:
        if curr_state[2][i] == 'X':
            return h_n + 1 # vehicle X detected
        elif curr_state[2][i] != '-':
            h_n += 2 # +1 for a vehicle, +1 for a distance
        else:
            h_n += 1 # +1 for a distance

# Calculate f(n) = g(n) + h(n)
# argument(s) : heuristic (0 or else), the current game board state, the number of actual paths
# return : if (heuristic == 0) -> zero for the goal state, or one plus the number of cars or trucks blocking the path to the exit for all other states.
#          else                -> zero for the goal state, or one plus the number of cars or trucks blocking the path to the exit for all other states plus the number of the distance from the goal.
def get_f_n(heuristic, curr_state, g_n):
    if (heuristic == 0):
        return blocking_heuristic(curr_state) + g_n
    else:
        return my_heuristic(curr_state) + g_n


# This is best-first search with A* algorithm
# argument(s) : heuristic (0 or else), the first state of the game board
# return : paths from the start state to the goal state (if a path exists), the number of total explored nodes
def best_first_search(heuristic, start_state):
    cnt_states_explored = 0
    g_n = 0
    f_n = get_f_n(heuristic, start_state, g_n)
    curr_state = Node(start_state, None, f_n, g_n)
    unexplored = [curr_state]
    explored = []

    while (unexplored != []):
        curr_state = unexplored.pop(0)
        g_n = curr_state.g_n + 1
        cnt_states_explored += 1
        explored.append(curr_state) # append to the explored list

        if (curr_state.goal_state()): # if current state is the goal state
            path = []
            path.append(curr_state.board)
            while (curr_state.prev_state != None):
                curr_state = curr_state.prev_state
                path.append(curr_state.board)
            return (path, cnt_states_explored)

        else: # if current state is NOT the goal state
            new_states_list = generate_new_states(curr_state, heuristic, g_n)
            for i in range(len(new_states_list)):
                if search_nodes(unexplored, new_states_list[i]):
                    continue
                elif search_nodes(explored, new_states_list[i]):
                    continue
                else:
                    unexplored.append(new_states_list[i])

        for i in range(len(unexplored)):
            unexplored.sort(key = sort_by_f)

    return ([], cnt_states_explored)

# This is the required function called by a user.
# argument(s) : heuristic(0 or else), the first state of the game board
# return : None (Prints the paths if a solution exists)
def rushhour(heuristic, start_state):
    path, total_explored = best_first_search(heuristic, start_state)
    if (path != []):
        path.reverse()
        for state in range(len(path)):
            print_state(path[state])
            print("") # This is for inserting a new empty line (so that output will be clear)
        print("Total moves: ", len(path) - 1) # We do not count the first state
        print("Total states explored: ", total_explored)
    else:
        print("No solution exists.") # For a case where the solution does not exist.


def main():
    # Test Cases
    test1 = ["--B---","--B---","XXB---","--AA--","------","------"]
    test3 = ["-----","------","XX----","------","------","------"]
    test3 = ["---O--","---O--","XX-O--","PQQQ--","P-----","P-----"]
    test4 = ["OOOP--","--AP--","XXAP--","Q-----","QGGCCD","Q----D"]
    test5 = ["--OPPP","--O--A","XXO--A","-CC--Q","-----Q","--RRRQ"]
    test6 = ["-ABBO-","-ACDO-","XXCDO-","PJFGG-","PJFH--","PIIH--"]
    test7 = ["OOO--P","-----P","--AXXP","--ABCC","D-EBFF","D-EQQQ"]
    test8 = ['------','------', 'E-XX--', 'E-----','------','------']
    test9 = ["---QQQ","OK----","OKXXB-","OK--B-","-L----","-L-GG-"]
    test10 = ["------","------","XX----","------","------","------"]

    # Call a test case
    print("****** Blocking Heuristic ******")
    print("")
    rushhour(0, test7) # This call is blocking heuristic
    print("\n")
    print("****** My Heuristic ******")
    print("")
    rushhour(1, test7) # This is my heuristic (explained details above)

if __name__ == "__main__":
    main()