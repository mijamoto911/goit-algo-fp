import heapq
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = {}
        self.distances = {}

    def add_vertex(self, vertex):
        self.vertices.add(vertex)
        self.edges[vertex] = []

    def add_edge(self, from_vertex, to_vertex, distance):
        self.edges[from_vertex].append(to_vertex)
        self.distances[(from_vertex, to_vertex)] = distance

    def dijkstra(self, start_vertex):
        priority_queue = [(0, start_vertex)]
        visited = set()

        while priority_queue:
            (current_distance, current_vertex) = heapq.heappop(priority_queue)

            if current_vertex in visited:
                continue

            visited.add(current_vertex)

            for neighbor in self.edges[current_vertex]:
                distance = current_distance + self.distances[(current_vertex, neighbor)]

                if neighbor not in visited:
                    heapq.heappush(priority_queue, (distance, neighbor))

        return visited

graph = Graph()

graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_vertex("E")

graph.add_edge("A", "B", 1)
graph.add_edge("B", "C", 2)
graph.add_edge("A", "D", 4)
graph.add_edge("D", "C", 3)
graph.add_edge("B", "E", 5)
graph.add_edge("C", "E", 1)

visited_vertices = graph.dijkstra("A")

print("The shortest paths from the top A:")
print(visited_vertices)
