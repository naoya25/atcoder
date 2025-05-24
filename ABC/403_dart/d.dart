import 'dart:io';
import 'dart:convert';
import 'dart:math';

void main() {
  final input = _Input();
  final [n, d] = input.getInts(2);
  final List<int> a = input.getInts(n);

  final Map<int, int> aCounter = {};
  for (final v in a) {
    aCounter[v] = (aCounter[v] ?? 0) + 1;
  }

  final List<int> aSorted = aCounter.keys.toList()..sort();

  if (d == 0) {
    final ans = aCounter.values.fold<int>(0, (sum, x) => sum + max(0, x - 1));
    print(ans);
    return;
  }

  int calc(List<int> xs) {
    if (xs.isEmpty) return 0;
    final x = [0, ...xs];
    final int m = x.length;
    final dp = List<int>.filled(m + 1, 0);
    for (int i = 1; i < m; i++) {
      dp[i + 1] = min(dp[i] + x[i], dp[i - 1] + x[i - 1]);
    }
    return dp[m];
  }

  int ans = 0;
  for (int r = 0; r < d; r++) {
    final sub = <int>[];
    for (final v in aSorted) {
      if (v % d == r) {
        sub.add(aCounter[v]!);
      }
    }
    ans += calc(sub);
  }

  print(ans);
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

extension IntList on List<int> {
  int max() => reduce((a, b) => a > b ? a : b);
  int min() => reduce((a, b) => a < b ? a : b);
  int sum() => reduce((a, b) => a + b);
  int product() => reduce((a, b) => a * b);
  void sortAsc() => sort((a, b) => a - b);
  void sortDesc() => sort((a, b) => b - a);
}
