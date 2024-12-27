# Battleship Q-Learning Simulation

This project implements a simulation of the classic game **Battleship** using Q-learning, a reinforcement learning algorithm. The game allows two AI agents to play against each other, improving their performance over time by learning from past experiences.

---

## Features
- **Random Ship Placement**: Ships are placed randomly on a 10x10 board while adhering to the game’s rules.
- **Q-Learning**: AI agents use Q-learning to decide the best moves during gameplay.
- **Performance Tracking**: Tracks the agents' learning progress and average accuracy over multiple simulations.

---

## File Structure
The project is divided into the following modules:

1. **`board.py`**
   - Contains functions for generating the game board and placing ships.
   - Functions:
     - `random_place_ships()`: Places ships randomly on the board.

2. **`q_learning.py`**
   - Implements Q-learning logic and helper functions.
   - Functions:
     - `reverse_map()`: Converts state to coordinates.
     - `get_available_shots()`: Retrieves legal shots.
     - `fire_shot_q()`: Chooses a shot based on Q-learning.
     - `shot_hit()`: Updates the reward and checks if a shot hit.
     - `q_learning()`: Updates Q-values based on the learning process.
     - `over()`: Checks if the game is over.
     - `copy_placements()`: Copies the ship placement board.
     - `run_round_q()`: Runs a round of Q-learning.
     - `average_results()`: Averages training results.

3. **`main.py`**
   - Contains the main simulation logic.
   - Initializes variables, runs the training loop, and tracks performance.

---

## Installation
1. **Clone the Repository**  
   ```bash
   git clone https://github.com/your-username/battleship-q-learning.git
   cd battleship-q-learning
