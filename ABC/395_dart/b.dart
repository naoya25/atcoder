import 'dart:io';
import 'dart:convert';

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

  int getIntZeroIndexed() {
    return getInt() - 1;
  }

  List<int> getInts(int n) {
    final result = <int>[];
    for (int i = 0; i < n; ++i) {
      result.add(getInt());
    }
    return result;
  }

  List<int> getIntsZeroIndexed(int n) {
    final result = <int>[];
    for (int i = 0; i < n; ++i) {
      result.add(getIntZeroIndexed());
    }
    return result;
  }

  double getDouble() {
    return double.parse(getString());
  }
}

void main() {
  final input = Input();
  int n = input.getInt();

  List<List<String>> grid = List.generate(
    n,
    (_) => List.generate(n, (_) => '#'),
  );

  for (int i = 0; i < n; i++) {
    int j = n - 1 - i;
    if (i <= j) {
      String t = i % 2 == 0 ? '#' : '.';
      for (int k = i; k <= j; ++k) {
        for (int l = i; l <= j; ++l) {
          grid[k][l] = t;
        }
      }
    }
  }

  for (int i = 0; i < n; i++) {
    print(grid[i].join(''));
  }
}
