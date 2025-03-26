import 'dart:io';
import 'dart:convert';

void main() {
  final input = Input();
  int n = input.getInt();
  List<int> a = input.getInts(n);

  List<(int, int)> pairs = [];
  for (int i = 0; i < a.length; i++) {
    pairs.add((i, a[i]));
  }

  pairs.sort((x, y) => y.$2 - x.$2);

  Map<int, int> counter = {};
  for (int val in a) {
    counter[val] = (counter[val] ?? 0) + 1;
  }

  for (final pair in pairs) {
    int idx = pair.$1;
    int val = pair.$2;

    if (counter[val] == 1) {
      print(idx + 1);
      return;
    }
  }

  print(-1);
}

class Input {
  final String data;
  int pos = 0;
  Input() : data = File('/dev/stdin').readAsStringSync(encoding: utf8);
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

  List<String> getStrings(int n) {
    final result = <String>[];
    // for (final _ in range(n)) {
    for (int i = 0; i < n; ++i) {
      result.add(getString());
    }
    return result;
  }

  int getInt() {
    return int.parse(getString());
  }

  List<int> getInts(int n) {
    final result = <int>[];
    // for (final _ in range(n)) {
    for (int i = 0; i < n; ++i) {
      result.add(getInt());
    }
    return result;
  }

  (List<int>, List<int>) getIntPairs(int n) {
    final a = <int>[];
    final b = <int>[];
    // for (final _ in range(n)) {
    for (int i = 0; i < n; ++i) {
      a.add(getInt());
      b.add(getInt());
    }
    return (a, b);
  }
}
