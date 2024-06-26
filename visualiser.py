import matplotlib.pyplot as plt
import networkx as nx

# Define the adjacency list
adjacency_list = {
    "0": [7],
    "1": [7, 8, 13],
    "2": [8, 9, 14],
    "3": [9, 10, 15],
    "4": [10, 11, 16],
    "5": [11, 12, 17],
    "6": [12],
    "7": [0, 1, 13, 18],
    "8": [1, 2, 13, 14, 19],
    "9": [2, 3, 14, 15, 20],
    "10": [3, 4, 15, 16, 21],
    "11": [4, 5, 16, 17, 22],
    "12": [5, 6, 17, 23],
    "13": [1, 7, 8, 18, 19, 24],
    "14": [2, 8, 9, 19, 20, 25],
    "15": [3, 9, 10, 20, 21, 26],
    "16": [4, 10, 11, 21, 22, 27],
    "17": [5, 11, 12, 22, 23, 28],
    "18": [7, 13, 24],
    "19": [8, 13, 14, 24, 25, 29],
    "20": [9, 14, 15, 25, 26, 30],
    "21": [10, 15, 16, 26, 27, 31],
    "22": [11, 16, 17, 27, 28, 32],
    "23": [12, 17, 28],
    "24": [13, 18, 19, 29, 33],
    "25": [14, 19, 20, 29, 30, 34],
    "26": [15, 20, 21, 30, 31, 35],
    "27": [16, 21, 22, 31, 32, 36],
    "28": [17, 22, 23, 32, 37],
    "29": [19, 24, 25, 33, 34, 38],
    "30": [20, 25, 26, 34, 35, 39],
    "31": [21, 26, 27, 35, 36, 40],
    "32": [22, 27, 28, 36, 37, 41],
    "33": [24, 29, 38],
    "34": [25, 29, 30, 38, 39, 42],
    "35": [26, 30, 31, 39, 40, 43],
    "36": [27, 31, 32, 40, 41, 44],
    "37": [28, 32, 41],
    "38": [29, 33, 34, 42, 45],
    "39": [30, 34, 35, 42, 43, 46],
    "40": [31, 35, 36, 43, 44, 47],
    "41": [32, 36, 37, 44, 48],
    "42": [34, 38, 39, 45, 46, 49],
    "43": [35, 39, 40, 46, 47, 50],
    "44": [36, 40, 41, 47, 48, 51],
    "45": [38, 42, 49],
    "46": [39, 42, 43, 49, 50, 52],
    "47": [40, 43, 44, 50, 51, 53],
    "48": [41, 44, 51],
    "49": [42, 45, 46, 52, 54],
    "50": [43, 46, 47, 52, 53, 55],
    "51": [44, 47, 48, 53, 56],
    "52": [46, 49, 50, 54, 55, 57],
    "53": [47, 50, 51, 55, 56, 58],
    "54": [49, 52, 57],
    "55": [50, 52, 53, 57, 58, 59],
    "56": [51, 53, 58],
    "57": [52, 54, 55, 59, 60],
    "58": [53, 55, 56, 59, 61],
    "59": [55, 57, 58, 60, 61, 62],
    "60": [57, 59, 62],
    "61": [58, 59, 62],
    "62": [59, 60, 61, 63],
    "63": [62]
}

# Create a graph from the adjacency list
G = nx.Graph(adjacency_list)

# Draw the graph
plt.figure(figsize=(10, 10))
nx.draw(G, with_labels=True, node_size=1000, node_color='lightblue', font_size=10, font_weight='bold')
plt.show()
