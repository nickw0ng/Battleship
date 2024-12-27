import numpy as np
import random
from board import random_place_ships
from q_learning import copy_placements, run_round_q, over

# Initialize parameters
nS = 100
nA = 100
total_size = 17
accuracy = []
e = 0.9

# Initialize Q-learning variables
Q1 = np.zeros((nS, nA))
R1 = np.zeros((nS, nS, nA))
U1 = np.zeros((nS, nA))

Q2 = np.zeros((nS, nA))
R2 = np.zeros((nS, nS, nA))
U2 = np.zeros((nS, nA))

# Create ships
ships1 = random_place_ships()
ships2 = random_place_ships()

# Training with Q-learning
for i in range(10000):
    s1 = random.randint(0, 99)
    s2 = random.randint(0, 99)
    num_rounds = 0
    your_ships = copy_placements(ships1)
    opponent_ships = copy_placements(ships2)
    while not over(your_ships, opponent_ships):
        s1 = run_round_q(s1, Q1, R1, U1, e, your_ships)
        s2 = run_round_q(s2, Q2, R2, U2, e, opponent_ships)
        e *= 0.99999
        num_rounds += 1
    accuracy.append(total_size / num_rounds)
