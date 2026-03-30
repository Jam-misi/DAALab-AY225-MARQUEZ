# Node Network Visualization and Shortest Path Analysis

## Overview

This program analyzes and visualizes a network of locations represented as nodes. Each node corresponds to a location (IMUS, BACOOR, DASMA, KAWIT, INDANG, SILANG, GENTRI, and NOVELETA), and the connections between them represent possible travel routes. Each route contains three attributes: **distance (km), travel time (minutes), and fuel consumption (liters)**.

The goal of the program is to construct a node map from the given data and determine the **most efficient path between two nodes** based on a selected metric.

## Approach

The first step in the implementation was identifying all unique locations from the dataset and storing them as nodes in a graph structure. The routes between locations were then stored as connections (edges) using a dictionary-based **adjacency list**, where each node keeps a list of neighboring nodes along with their attributes (distance, time, and fuel).

To represent the node map, the program prints a structured text representation showing how each node connects to other nodes and the associated travel attributes. This approach allows the relationships between nodes to be clearly displayed without requiring external visualization libraries.

## Algorithm Used

The program uses **Dijkstra’s Algorithm** to compute the shortest path between two nodes. This algorithm works by repeatedly selecting the node with the smallest current cost and updating the distances of its neighboring nodes.

A **priority queue (implemented using Python’s built-in `heapq` module)** is used to efficiently retrieve the node with the lowest cost during each iteration. The algorithm continues until the destination node is reached. The cost can be calculated based on one of three criteria:

* Distance
* Travel Time
* Fuel Consumption

After the shortest path is found, the program calculates the total distance, total time, and total fuel consumption for the selected route.

## Challenges Encountered

One of the main challenges in this assignment was properly organizing the graph structure so that each route contained multiple attributes while still allowing the algorithm to optimize based on a single chosen metric. Another challenge was ensuring the path reconstruction worked correctly so that the program could display the full route from the starting node to the destination node instead of only showing numerical distances.

Additionally, the program was designed to work **without requiring external libraries**, so a text-based node map representation was used instead of graphical visualization.

## Conclusion

The final program successfully constructs a node network from the provided data and uses Dijkstra’s Algorithm to determine the most efficient path between locations based on distance, time, or fuel consumption. The output clearly displays the selected path along with the total distance, time, and fuel required, allowing users to analyze different route optimization scenarios.
