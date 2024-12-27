import numpy as np
import random
from board import random_place_ships

# Reverses a state to a coordinate
def reverse_map(observation):
    return observation // 10, observation % 10

# Gets the available shots
def get_available_shots(ships):
    shots = []
    for i in range(100):
        x, y = reverse_map(i)
        if ships[x][y] != 1:
            shots.append(i)
    return shots

# Fires a shot using Q-learning
def fire_shot_q(state, epsilon, Q, ships):
    legal_shots = get_available_shots(ships)
    chance = np.random.rand()
    if chance < epsilon:
        return np.random.choice(legal_shots)
    max_action = legal_shots[0]
    for a in legal_shots:
        if Q[state][a] > Q[state][max_action]:
            max_action = a
    return max_action

# Determines if a shot hit a ship
# Updates the Reward and ship
def shot_hit(a, s, ships, R):
    x, y = reverse_map(a)
    tile = ships[x][y]
    ships[x][y] = 1
    if tile == 2:
        R[a][s][a] += 50
        return True
    return False

# Performs Q-learning
def q_learning(a, s, ships, R, U, Q, gamma):
    shot_hit(a, s, ships, R)
    learning_rate = 1 / (1 + U[s, a])
    Q[s][a] = Q[s][a] + learning_rate * (R[a][s][a] + gamma * np.max(Q[a]) - Q[s][a])
    U[s][a] += 1

# Checks if the game is over
def over(your_ships, opponent_ships):
    return 2 not in your_ships or 2 not in opponent_ships

# Copies the placements of ships
def copy_placements(ships):
    return np.copy(ships)

# Runs a round of Q-learning
def run_round_q(s, Q, R, U, e, ships):
    a = fire_shot_q(s, e, Q, ships)
    q_learning(a, s, ships, R, U, Q, gamma=0.9)
    return a

# Averages the results of training based on a given interval
def average_results(results, step):
    average_results = []
    for i in range(len(results)):
        if i % step == 0 and i > 0:
            average_results.append(np.mean(results[i - step:i]))
    return average_results
