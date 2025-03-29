import 'dart:io';
import 'dart:convert';

void main() {
  final input = Input();
  final [n, m] = input.getInts(2);

  final graph = UndirectedGraph(n);
  for (int i = 0; i < m; ++i) {
    final [u, v] = input.getInts0idx(2);
    graph.addEdge(u, v);
  }

  final visited = List<bool>.filled(n, false);
  int count = 0;
  for (int i = 0; i < n; i++) {
    if (!visited[i]) {
      count++;
      graph.dfs(i, visited);
    }
  }

  print(m - n + count);
}

class Input {
  static Input? _instance;
  Input._() : data = File('/dev/stdin').readAsStringSync(encoding: utf8);

  factory Input() {
    _instance ??= Input._();
    return _instance!;
  }

  final String data;
  int pos = 0;

  bool isSpace(String ch) {
    return ch == " " || ch == "\n";
  }

  String getString() {
    var p = pos;
    while (p < data.length && isSpace(data[p])) p++;
    final from = p;
    while (p < data.length && !isSpace(data[p])) p++;
    final to = p;
    pos = p;
    return data.substring(from, to);
  }

  List<String> getStringAsList() {
    return getString().split('');
  }

  List<String> getStrings(int n) {
    final result = <String>[];
    for (int i = 0; i < n; ++i) {
      result.add(getString());
    }
    return result;
  }

  int getInt() {
    return int.parse(getString());
  }

  int getInt0idx() {
    return getInt() - 1;
  }

  List<int> getInts(int n) {
    final result = <int>[];
    for (int i = 0; i < n; ++i) {
      result.add(getInt());
    }
    return result;
  }

  List<int> getInts0idx(int n) {
    final result = <int>[];
    for (int i = 0; i < n; ++i) {
      result.add(getInt0idx());
    }
    return result;
  }

  double getDouble() {
    return double.parse(getString());
  }

  List<List<int>> getInt2d(int n, int m) {
    final result = <List<int>>[];
    for (int i = 0; i < n; ++i) {
      result.add(getInts(m));
    }
    return result;
  }
}

void printBool(bool b) {
  print(b ? 'Yes' : 'No');
}

void printList(List list, {String separator = ' '}) {
  print(list.join(separator));
}

// 辺
class Edge {
  final int from;
  final int to;
  final int weight;

  Edge(this.from, this.to, this.weight);

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
