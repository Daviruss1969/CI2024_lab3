from random import choice
from dataclasses import dataclass, field
from heapq import heappop, heappush
import numpy as np

PUZZLE_DIM = 6
RANDOMIZE_STEPS = 100_000
SOLUTION = np.ndarray([])
TARGET_POSITIONS = dict()

@dataclass
class Action:
    src: int
    dst: int

@dataclass(order=True)
class Node:
    priority: int
    state: list[list[int]] = field(compare=False)
    step: int = field(compare=False)

def available_actions(state: np.ndarray) -> list[Action]:
    """Returns all the possible actions for a given state"""
    x, y = np.argwhere(state == 0)[0] # Get the indexes of the 0 in the puzzle

    # Add all possible actions by checking boundaries
    actions = list()
    if x > 0:
        actions.append(Action((x, y), (x - 1, y)))
    if x < PUZZLE_DIM - 1:
        actions.append(Action((x, y), (x + 1, y)))
    if y > 0:
        actions.append(Action((x, y), (x, y - 1)))
    if y < PUZZLE_DIM - 1:
        actions.append(Action((x, y), (x, y + 1)))
    return actions


def do_action(state: np.ndarray, action: Action) -> np.ndarray:
    """Returns a new state that perform the given action on a given state"""
    new_state = state.copy()
    new_state[action.src], new_state[action.dst] = new_state[action.dst], new_state[action.src]
    return new_state

def init_problem() -> np.ndarray[np.ndarray[int]]:
    """Return a N-puzzle problem and its solution where N is given by PUZZLE_DIM"""
    solution = np.array([i for i in range(1, PUZZLE_DIM**2)] + [0]).reshape((PUZZLE_DIM, PUZZLE_DIM)) # Create matrix

    # Randomize it
    state = solution.copy()
    for _ in range(RANDOMIZE_STEPS):
        state = do_action(state, choice(available_actions(state)))

    return state, solution

def precompute_target_positions() -> dict[int, tuple[int, int]]:
    """Return a dictionary that contains the target indexes of one entry of the n-puzzle"""
    target_positions = {}
    for x in range(PUZZLE_DIM):
        for y in range(PUZZLE_DIM):
            target_positions[SOLUTION[x, y]] = (x, y)
    return target_positions

def manhattan_distance(state: np.ndarray) -> int:
    """Compute the manhattan distance bewteen a state and the solution"""
    total_distance = 0

    # Sum each difference of distances
    for x in range(PUZZLE_DIM):
        for y in range(PUZZLE_DIM):
            value = state[x, y]
            if value == 0:
                continue  # Skip tile 0
            target_x, target_y = TARGET_POSITIONS[value]
            total_distance += abs(target_x - x) + abs(target_y - y)

    return total_distance

from heapq import heappop, heappush

def n_puzzle_gbf(state):
    """Return the solution of an N puzzle for a given initial state"""
    frontier: list[Node] = [] # Use a heap for storing the states
    heappush(frontier, Node(manhattan_distance(state), state, 0))
    explored = set()
    cost = 0

    while frontier:
        cost += 1
        current_node = heappop(frontier) # Get the node with the maximum expected value

        # Goal test
        if np.array_equal(SOLUTION, current_node.state):
            return current_node.state, current_node.step, cost

        # Explore all possible actions
        for action in available_actions(current_node.state):
            new_state = do_action(current_node.state, action)

            # Check for state already explored
            new_tuple = tuple(map(tuple, new_state))
            if new_tuple in explored:
                continue
            explored.add(new_tuple)

            heappush(frontier, Node(manhattan_distance(new_state), new_state, current_node.step + 1))

    return None, None, cost

state, SOLUTION = init_problem()
TARGET_POSITIONS = precompute_target_positions()

# Perform algorithm
final_state, quality, cost = n_puzzle_gbf(state.copy())

# Show results
if final_state is None:
    print("No solutions founded")
else:
    print("Quality of the solution :", quality, "cost of the solution :", cost)