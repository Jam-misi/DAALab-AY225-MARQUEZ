import heapq

# -----------------------------
# Graph Data (Distance, Time, Fuel)
# -----------------------------
edges = [
    ("IMUS","BACOOR",10,15,1.2),
    ("BACOOR","DASMA",12,25,1.5),
    ("DASMA","KAWIT",12,25,1.5),
    ("KAWIT","INDANG",12,25,1.2),
    ("INDANG","SILANG",14,25,1.5),
    ("SILANG","GENTRI",10,25,1.3),
    ("GENTRI","NOVELETA",10,25,1.5),
    ("NOVELETA","IMUS",10,15,1.2),
    ("BACOOR","SILANG",10,25,1.3),
    ("DASMA","SILANG",12,25,1.5),
    ("SILANG","BACOOR",10,25,1.3),
    ("NOVELETA","BACOOR",10,15,1.2),
    ("SILANG","KAWIT",14,25,1.2),
    ("IMUS","NOVELETA",10,15,1.2)
]

# -----------------------------
# Build Graph Structure
# -----------------------------
graph = {}

for u, v, d, t, f in edges:
    graph.setdefault(u, {})
    graph.setdefault(v, {})

    graph[u][v] = {"distance": d, "time": t, "fuel": f}
    graph[v][u] = {"distance": d, "time": t, "fuel": f}


# -----------------------------
# Display Node Map (Text Version)
# -----------------------------
def show_node_map(graph):

    print("\nNODE MAP")
    print("-"*40)

    for node in graph:
        print(f"{node} connects to:")

        for neighbor, attr in graph[node].items():
            print(f"   -> {neighbor} | Distance:{attr['distance']} km | Time:{attr['time']} min | Fuel:{attr['fuel']} L")

        print()


# -----------------------------
# Dijkstra Shortest Path
# -----------------------------
def shortest_path(graph, start, end, metric):

    pq = [(0, start, [])]
    visited = set()

    while pq:

        cost, node, path = heapq.heappop(pq)

        if node in visited:
            continue

        path = path + [node]
        visited.add(node)

        if node == end:
            return cost, path

        for neighbor, attr in graph[node].items():
            if neighbor not in visited:
                heapq.heappush(pq, (cost + attr[metric], neighbor, path))

    return float("inf"), []


# -----------------------------
# Calculate totals of path
# -----------------------------
def calculate_totals(graph, path):

    total_distance = 0
    total_time = 0
    total_fuel = 0

    for i in range(len(path)-1):
        edge = graph[path[i]][path[i+1]]

        total_distance += edge["distance"]
        total_time += edge["time"]
        total_fuel += edge["fuel"]

    return total_distance, total_time, total_fuel


# -----------------------------
# Program Execution
# -----------------------------
show_node_map(graph)

start = "IMUS"
end = "INDANG"

metric = "distance"   # choose: distance, time, fuel

cost, path = shortest_path(graph, start, end, metric)

distance, time, fuel = calculate_totals(graph, path)

print("\nSHORTEST PATH RESULT")
print("-"*40)

print("Path:", " -> ".join(path))
print("Total Distance:", distance, "km")
print("Total Time:", time, "mins")
print("Total Fuel:", fuel, "liters")