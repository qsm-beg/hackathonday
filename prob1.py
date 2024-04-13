import itertools

# Define the garden
garden = {
    "0": [0, 0], "1": [0, 2], "2": [0, 4], "3": [0, 6], "4": [0, 8], "5": [0, 10], "6": [0, 12],
    "7": [0, 1], "8": [0, 3], "9": [0, 5], "10": [0, 7], "11": [0, 9], "12": [0, 11],
    "13": [1, 2], "14": [1, 4], "15": [1, 6], "16": [1, 8], "17": [1, 10], 
    "18": [1, 1], "19": [1, 3], "20": [1, 5], "21": [1, 7], "22": [1, 9], "23": [1, 11],
    "24": [2, 2], "25": [2, 4], "26": [2, 6], "27": [2, 8], "28": [2, 10], 
    "29": [2, 3], "30": [2, 5], "31": [2, 7], "32": [2, 9], 
    "33": [3, 2], "34": [3, 4], "35": [3, 6], "36": [3, 8], "37": [3, 10], 
    "38": [3, 3], "39": [3, 5], "40": [3, 7], "41": [3, 9], 
    "42": [4, 4], "43": [4, 6], "44": [4, 8], "45": [4, 3], "46": [4, 5], "47": [4, 7], "48": [4, 9], 
    "49": [5, 4], "50": [5, 6], "51": [5, 8], "52": [5, 5], "53": [5, 7], 
    "54": [6, 4], "55": [6, 6], "56": [6, 8], "57": [6, 5], "58": [6, 7], 
    "59": [7, 6], "60": [7, 5], "61": [7, 7], 
    "62": [8, 6], 
    "63": [9, 6]
}

# Define the adjacency list
adjacency_list = {
    "0": [7], "1": [7, 8, 13], "2": [8, 9, 14], "3": [9, 10, 15], "4": [10, 11, 16], "5": [11, 12, 17], 
    "6": [12], "7": [0, 1, 13, 18], "8": [1, 2, 13, 14, 19], "9": [2, 3, 14, 15, 20], "10": [3, 4, 15, 16, 21], 
    "11": [4, 5, 16, 17, 22], "12": [5, 6, 17, 23], "13": [1, 7, 8, 18, 19, 24], "14": [2, 8, 9, 19, 20, 25], 
    "15": [3, 9, 10, 20, 21, 26], "16": [4, 10, 11, 21, 22, 27], "17": [5, 11, 12, 22, 23, 28], 
    "18": [7, 13, 24], "19": [8, 13, 14, 24, 25, 29], "20": [9, 14, 15, 25, 26, 30], "21": [10, 15, 16, 26, 27, 31], 
    "22": [11, 16, 17, 27, 28, 32], "23": [12, 17, 28], "24": [13, 18, 19, 29, 33], "25": [14, 19, 20, 29, 30, 34], 
    "26": [15, 20, 21, 30, 31, 35], "27": [16, 21, 22, 31, 32, 36], "28": [17, 22, 23, 32, 37], 
    "29": [19, 24, 25, 33, 34, 38], "30": [20, 25, 26, 34, 35, 39], "31": [21, 26, 27, 35, 36, 40], 
    "32": [22, 27, 28, 36, 37, 41], "33": [24, 29, 38], "34": [25, 29, 30, 38, 39, 42], 
    "35": [26, 30, 31, 39, 40, 43], "36": [27, 31, 32, 40, 41, 44], "37": [28, 32, 41], 
    "38": [29, 33, 34, 42, 45], "39": [30, 34, 35, 42, 43, 46], "40": [31, 35, 36, 43, 44, 47], 
    "41": [32, 36, 37, 44, 48], "42": [34, 38, 39, 45, 46, 49], 
    "43": [35, 39, 40, 46, 47, 50], "44": [36, 40, 41, 47, 48, 51], 
    "45": [38, 42, 49], "46": [39, 42, 43, 49, 50, 52], "47": [40, 43, 44, 50, 51, 53], 
    "48": [41, 44, 51], "49": [42, 45, 46, 52, 54], "50": [43, 46, 47, 52, 53, 55], 
    "51": [44, 47, 48, 53, 56], "52": [46, 49, 50, 54, 55, 57], "53": [47, 50, 51, 55, 56, 58], 
    "54": [49, 52, 57], "55": [50, 52, 53, 57, 58, 59], "56": [51, 53, 58], 
    "57": [52, 54, 55, 59, 60], "58": [53, 55, 56, 59, 61], "59": [55, 57, 58, 60, 61, 62], 
    "60": [57, 59, 62], "61": [58, 59, 62], "62": [59, 60, 61, 63], "63": [62]
}

# Define the herb and sprinkler combinations
herb_combinations = [
    ("Basil", {"sunlight": "High", "water": "Moderate"}),
    ("Rosemary", {"sunlight": "High", "water": "Low"}),
    ("Mint", {"sunlight": "Moderate", "water": "High"}),
    ("Parsley", {"sunlight": "Moderate", "water": "Moderate"}),
    ("Thyme", {"sunlight": "Low", "water": "Low"})
]

sprinkler_combinations = [
    ("Sprinkler A", {"coverage": "Small"}),
    ("Sprinkler B", {"coverage": "Medium"}),
    ("Sprinkler C", {"coverage": "Large"})
]

# Define profit values for each herb-sprinkler combination
profits = {
    ("Basil", "Sprinkler A"): 10,
    ("Basil", "Sprinkler B"): 15,
    ("Basil", "Sprinkler C"): 20,
    ("Rosemary", "Sprinkler A"): 12,
    ("Rosemary", "Sprinkler B"): 18,
    ("Rosemary", "Sprinkler C"): 24,
    ("Mint", "Sprinkler A"): 8,
    ("Mint", "Sprinkler B"): 12,
    ("Mint", "Sprinkler C"): 16,
    ("Parsley", "Sprinkler A"): 6,
    ("Parsley", "Sprinkler B"): 9,
    ("Parsley", "Sprinkler C"): 12,
    ("Thyme", "Sprinkler A"): 4,
    ("Thyme", "Sprinkler B"): 6,
    ("Thyme", "Sprinkler C"): 8
}

# Function to calculate profit for placing a herb and sprinkler combination
def calculate_profit(herb, sprinkler):
    return profits.get((herb, sprinkler), 0)

# Function to calculate the total profit for a garden configuration
def calculate_total_profit(placement):
    total_profit = 0
    for hexagon, (herb, sprinkler) in placement.items():
        total_profit += calculate_profit(herb, sprinkler)
    return total_profit

# Function to find the best herb and sprinkler combination for a hexagon
def find_best_combination(hexagon):
    best_profit = 0
    best_combination = None
    for herb, sprinkler in itertools.product(herb_combinations, sprinkler_combinations):
        profit = calculate_profit(herb[0], sprinkler[0])
        if profit > best_profit:
            best_profit = profit
            best_combination = (herb[0], sprinkler[0])
    return best_combination

# Main optimization function
def optimize_garden():
    placement = {}  # Dictionary to store the final placement of herbs and sprinklers

    for hexagon, adjacent_hexagons in adjacency_list.items():
        best_combination = find_best_combination(hexagon)
        placement[hexagon] = best_combination

    return placement

# Run the optimization
optimized_placement = optimize_garden()

# Print the optimized placement
print(optimized_placement)
