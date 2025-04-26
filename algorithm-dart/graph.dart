// 辺
class Edge {
  Edge(this.from, this.to, this.weight);

  final int from;
  final int to;
  final int weight;

  @override
  bool operator ==(Object other) =>
      other is Edge &&
      from == other.from &&
      to == other.to &&
      weight == other.weight;

  @override
  int get hashCode => Object.hash(from, to, weight);

  @override
  String toString() => 'Edge($from -> $to: $weight)';
}

// 無向グラフ (0-indexed)
class UndirectedGraph {
  UndirectedGraph(int n) : _adj = Map(), _n = n;

  final Map<int, Set<Edge>> _adj;
  final int _n;

  int get n => _n;
  Map<int, Set<Edge>> get adj => _adj;

  void addEdge(int from, int to, [int weight = 1]) {
    if (!_adj.containsKey(from)) _adj[from] = <Edge>{};
    if (!_adj.containsKey(to)) _adj[to] = <Edge>{};

    _adj[from]?.add(Edge(from, to, weight));
    _adj[to]?.add(Edge(to, from, weight));
  }

  Set<Edge> getEdges(int node) {
    return _adj[node] ?? <Edge>{};
  }

  List<List<Edge>> getPathsWithEdges(int start, int end) {
    List<List<Edge>> paths = [];
    List<Edge> currentPath = [];
    List<bool> visited = List.filled(_n, false);
    visited[start] = true;

    List<(int, int)> stack = [];
    stack.add((start, 0));

    while (!stack.isEmpty) {
      var (node, edgeIndex) = stack.last;
      List<Edge> edges = (_adj[node]?.toList() ?? []);

      if (edgeIndex >= edges.length) {
        stack.removeLast();
        visited[node] = false;
        if (currentPath.isNotEmpty) {
          currentPath.removeLast();
        }
        continue;
      }

      Edge edge = edges[edgeIndex];
      stack[stack.length - 1] = (node, edgeIndex + 1);
      int nextNode = edge.to;

      if (visited[nextNode]) continue;

      currentPath.add(edge);
      visited[nextNode] = true;
      if (nextNode == end) {
        paths.add(List.from(currentPath));
        visited[nextNode] = false;
        currentPath.removeLast();
      } else {
        stack.add((nextNode, 0));
      }
    }
    return paths;
  }

  void dfs(int startNode, List<bool> visited) {
    final stack = <int>[];
    stack.add(startNode);
    visited[startNode] = true;

    while (stack.isNotEmpty) {
      final node = stack.removeLast();

      for (Edge edge in getEdges(node)) {
        if (!visited[edge.to]) {
          visited[edge.to] = true;
          stack.add(edge.to);
        }
      }
    }
  }
}

// 有向グラフ (0-indexed)
class DirectedGraph {
  DirectedGraph(int n) : _adj = Map(), _n = n;

  final Map<int, Set<Edge>> _adj;
  final int _n;

  int get n => _n;
  Map<int, Set<Edge>> get adj => _adj;

  void addEdge(int from, int to, [int weight = 1]) {
    if (!_adj.containsKey(from)) _adj[from] = <Edge>{};
    _adj[from]?.add(Edge(from, to, weight));
  }

  Set<Edge> getEdges(int node) {
    return _adj[node] ?? <Edge>{};
  }
}
