import 'dart:io';
import 'dart:convert';

void main() {
  final input = Input();
  int t = input.getInt();

  for (int tc = 0; tc < t; tc++) {
    int n = input.getInt();
    List<int> a = input.getInts(2 * n);

    List<List<int>> position = List.generate(n + 1, (_) => []);
    for (int i = 0; i < 2 * n; i++) {
      position[a[i]].add(i);
    }

    Set<Pair> answers = {};
    for (int i = 0; i + 1 < 2 * n; i++) {
      int x = a[i], y = a[i + 1];
      if (position[x][0] + 1 == position[x][1]) continue;
      if (position[y][0] + 1 == position[y][1]) continue;

      List<int> v = [
        position[x][0],
        position[x][1],
        position[y][0],
        position[y][1],
      ];
      v.sort();

      if (v[0] + 1 == v[1] && v[2] + 1 == v[3]) {
        int minVal = x < y ? x : y;
        int maxVal = x < y ? y : x;
        answers.add(Pair(minVal, maxVal));
      }
    }
    print(answers.length);
  }
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

class Pair {
  int first;
  int second;

  Pair(this.first, this.second);

  @override
  bool operator ==(Object other) =>
      identical(this, other) ||
      other is Pair &&
          runtimeType == other.runtimeType &&
          first == other.first &&
          second == other.second;

  @override
  int get hashCode => first.hashCode ^ second.hashCode;
}
