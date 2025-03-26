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

  List<int> getInts(int n) {
    final result = <int>[];
    for (int i = 0; i < n; ++i) {
      result.add(getInt());
    }
    return result;
  }

  double getDouble() {
    return double.parse(getString());
  }
}

// 座標(x, y)
class Point {
  int x;
  int y;

  Point(this.x, this.y);

  @override
  bool operator ==(Object other) =>
      other is Point && other.x == x && other.y == y;

  @override
  int get hashCode => Object.hash(x, y);

  @override
  String toString() => '$x, $y';
}

void main() {
  final input = Input();
  int n = input.getInt();
  List<int> a = input.getInts(n);

  List<int> headVariety = List.filled(n - 1, 0);
  List<int> tailVariety = List.filled(n - 1, 0);

  Set<int> headKeys = {};
  Set<int> tailKeys = {};

  for (int i = 0; i < n - 1; ++i) {
    headKeys.add(a[i]);
    headVariety[i] = headKeys.length;

    tailKeys.add(a[n - i - 1]);
    tailVariety[n - i - 2] = tailKeys.length;
  }

  int ans = 0;
  for (int i = 0; i < n - 1; ++i) {
    int t = headVariety[i] + tailVariety[i];
    if (t > ans) {
      ans = t;
    }
  }

  print(ans);
}
