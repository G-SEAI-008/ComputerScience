class DirectedGraph:
    def __init__(self, labels):
        self.labels = labels
        self.num_vertices = len(labels)
        self.adj_matrix = [[0] * self.num_vertices for _ in range(self.num_vertices)]

    def label_to_index(self, label):
        if label not in self.labels:
            raise ValueError(f"Label {label} not found in the graph")
        return self.labels.index(label)

    def add_edge(self, label_from, label_to, weight=1):
        u = self.label_to_index(label_from)
        v = self.label_to_index(label_to)
        self.adj_matrix[u][v] = weight

    def remove_edge(self, label_from, label_to):
        u = self.label_to_index(label_from)
        v = self.label_to_index(label_to)
        self.adj_matrix[u][v] = 0

    def print_matrix(self):
        header = "    " + "  ".join(self.labels)
        print(header)
        for i, row in enumerate(self.adj_matrix):
            row_str = "  ".join(str(x) for x in row)
            print(f"{self.labels[i]}   {row_str}")

    def detect_cycle_dfs(self):
        visited = [False] * self.num_vertices
        rec_stack = [False] * self.num_vertices

        def dfs(curr):
            visited[curr] = True
            rec_stack[curr] = True

            for neighbor in range(self.num_vertices):
                if self.adj_matrix[curr][neighbor] != 0:
                    if not visited[neighbor]:
                        if dfs(neighbor):
                            return True
                    elif rec_stack[neighbor]:
                        return True
            rec_stack[curr] = False

        for vertex in range(self.num_vertices):
            if not visited[vertex]:
                if dfs(vertex):
                    return True
        return False


labels = ["A", "B", "C", "D", "E", "F"]

graph = DirectedGraph(labels)


graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("D", "C")
graph.add_edge("C", "F")
graph.add_edge("C", "E")

graph.detect_cycle_dfs()

# graph.print_matrix()
# Füge Verbindung zwischen A und C hinzu


class UndirectedGraph:
    def __init__(self, labels):
        self.labels = labels
        self.num_vertices = len(labels)
        self.adj_matrix = [[0] * self.num_vertices for _ in range(self.num_vertices)]

    def label_to_index(self, label):
        if label not in self.labels:
            raise ValueError(f"Label {label} not found in the graph")
        return self.labels.index(label)

    def add_edge(self, label_from, label_to, weight=1):
        u = self.label_to_index(label_from)
        v = self.label_to_index(label_to)
        self.adj_matrix[u][v] = weight
        self.adj_matrix[v][u] = weight

    def remove_edge(self, label_from, label_to):
        u = self.label_to_index(label_from)
        v = self.label_to_index(label_to)
        self.adj_matrix[u][v] = 0
        self.adj_matrix[v][u] = 0

    def print_matrix(self):
        header = "    " + "  ".join(self.labels)
        print(header)
        for i, row in enumerate(self.adj_matrix):
            row_str = "  ".join(str(x) for x in row)
            print(f"{self.labels[i]}   {row_str}")

    def bfs(self, start_label):
        visited = set()
        queue = []

        queue.append(start_label)
        visited.add(start_label)

        while queue:
            current_label = queue.pop(0)
            print(current_label)
            current_index = self.label_to_index(current_label)

            for neighbor_index, is_connected in enumerate(
                self.adj_matrix[current_index]
            ):
                neighbor_label = self.labels[neighbor_index]
                if is_connected and neighbor_label not in visited:
                    queue.append(neighbor_label)
                    visited.add(neighbor_label)

    def dfs(self, start_label):
        visited = set()

        def dfs_helper(label):
            print(label)
            visited.add(label)
            start_index = self.label_to_index(label)

            for neighbor_index, is_connected in enumerate(self.adj_matrix[start_index]):
                neighbor_label = self.labels[neighbor_index]
                if is_connected and neighbor_label not in visited:
                    dfs_helper(neighbor_label)

        dfs_helper(start_label)

    def detect_cycle_dfs(self):
        visited = [False] * self.num_vertices

        def dfs(curr, parent):
            visited[curr] = True

            for neighbor in range(self.num_vertices):
                if self.adj_matrix[curr][neighbor] != 0:
                    if not visited[neighbor]:
                        if dfs(neighbor, curr):
                            return True
                    elif neighbor != parent:
                        return True
            return False

        for vertex in range(self.num_vertices):
            if not visited[vertex]:
                if dfs(vertex, -1):
                    return True
        return False


unGraph = UndirectedGraph(["A", "B", "C", "D", "E", "F"])


unGraph.add_edge("A", "B")
unGraph.add_edge("A", "C")
unGraph.add_edge("B", "D")
unGraph.add_edge("D", "C")
unGraph.add_edge("C", "F")
unGraph.add_edge("C", "E")

# print("bfs")
# unGraph.bfs("A")

# print("dfs")
# unGraph.dfs("A")

unGraph.detect_cycle_dfs()
# unGraph.print_matrix()
