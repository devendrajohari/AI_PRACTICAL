from queue import PriorityQueue

class Graph:
    def __init__(self, vertices):
        self.graph = [[] for i in range(vertices)]

    def add_edge(self, x, y, cost):
        self.graph[x].append((y, cost))
        self.graph[y].append((x, cost))
        print(self.graph)

    def best_first_search(self, source, target, vertices):
        visited = [0]*vertices
        pq = PriorityQueue()
        pq.put((0, source))
        print("Path : ")
        while not pq.empty():
            u = pq.get()[1]
            print(u, end="")
            if u == target:
                break

            for v,c in self.graph[u]:
                if not visited[v]:
                    visited[v] = True
                    pq.put((c, v))

    print()

vertices = 14
graph1 = Graph(vertices)
graph1.add_edge(0, 1, 1)
graph1.add_edge(0, 2, 8)
graph1.add_edge(1, 2, 12)
graph1.add_edge(1, 4, 13)
graph1.add_edge(2, 3, 6)
graph1.add_edge(4, 3, 3)

source =0
target=2
graph1.best_first_search(source, target, vertices)