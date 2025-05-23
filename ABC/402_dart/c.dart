import 'dart:io';
import 'dart:convert';

void main() {
  final input = _Input();
  final nm = input.getInts(2);
  final int n = nm[0], m = nm[1];

  final List<int> remaining = List.filled(m, 0);
  final Map<int, List<int>> foodToDishes = {};

  for (int dishIdx = 0; dishIdx < m; dishIdx++) {
    int k = input.getInt();
    final a = input.getInts(k).toSet();
    remaining[dishIdx] = a.length;
    for (var f in a) {
      foodToDishes.putIfAbsent(f, () => []).add(dishIdx);
    }
  }

  final List<int> b = input.getInts(n);

  final Set<int> eaten = {};
  int ans = 0;

  for (int i = 0; i < n; i++) {
    int f = b[i];
    if (eaten.add(f)) {
      final list = foodToDishes[f];
      if (list != null) {
        for (var dishIdx in list) {
          remaining[dishIdx]--;
          if (remaining[dishIdx] == 0) {
            ans++;
          }
        }
      }
    }
    print(ans);
  }
}

class _Input {
  static _Input? _instance;
  _Input._() : data = File('/dev/stdin').readAsStringSync(encoding: utf8);

  factory _Input() {
    _instance ??= _Input._();
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

  List<List<String>> getStrings2d(int n, int m) {
    final result = <List<String>>[];
    for (int i = 0; i < n; ++i) {
      result.add(getStringAsList());
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
