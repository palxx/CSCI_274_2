class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.edges = []    # List to store graph edges

    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))

    def bellman_ford_moore(self, src):
        # Step 1: Initialize distances from src to all other vertices as infinity
        dist = [float('inf')] * self.V
        dist[src] = 0

        # Step 2: Initialize a successor list to track the path
        successor = [None] * self.V

        # Step 3: Relax edges up to V-1 times with early stopping
        count = 0
        for i in range(self.V - 1):
            updated = False  # Track if any update happened in this pass

            for u, v, weight in self.edges:
                count+=1
                # Relax the edge if possible
                if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    successor[v] = u
                    updated = True  # Mark that an update happened

            # If no update occurred in this pass, stop early
            if not updated:
                print(f"Algorithm stopped early at iteration {i + 1}")
                break
        print('count', count)

        # Step 4: Check for negative-weight cycles
        for u, v, weight in self.edges:
            if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                print("Graph contains a negative weight cycle")
                return None

        # Print the final distances
        self.print_solution(dist, successor)

    def print_solution(self, dist, successor):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print(f"{i}\t\t{dist[i]} (via {successor[i]})")

# Driver code to test the above implementation
if __name__ == "__main__":
    # Create a graph with 5 vertices
    g = Graph(5)
    g.add_edge(0, 1, -1)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 2)
    g.add_edge(1, 4, 2)
    g.add_edge(3, 2, 5)
    g.add_edge(3, 1, 1)
    g.add_edge(4, 3, -3)

    # Run Bellman-Ford-Moore algorithm from source vertex 0
    g.bellman_ford_moore(0)
