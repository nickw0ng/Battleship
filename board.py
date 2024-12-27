import numpy as np
import random

# Each type of ship and their size
ships = {
    "Carrier": 5,
    "Battleship": 4,
    "Cruiser": 3,
    "Submarine": 3,
    "Destroyer": 2
}

# Randomly places ships on a board
def random_place_ships():
    your_ships = np.zeros((10, 10))
    for ship in ships:
        ship_size = ships[ship]
        right_placements = []
        down_placements = []
        for x in range(10):
            for y in range(10):
                end_d = x + ship_size
                end_r = y + ship_size
                if end_d <= 10 and 2 not in your_ships[:, y][x:end_d]:
                    down_placements.append((x, y))
                if end_r <= 10 and 2 not in your_ships[x][y:end_r]:
                    right_placements.append((x, y))
        if len(down_placements) > 0 and len(right_placements) > 0:
            d_or_r = random.randint(0, 1)
            if d_or_r == 1:
                x, y = down_placements[random.randint(0, len(down_placements) - 1)]
                end = x + ship_size
                your_ships[:, y][x:end] = 2
            else:
                x, y = right_placements[random.randint(0, len(right_placements) - 1)]
                end = y + ship_size
                your_ships[x][y:end] = 2

    return your_ships
