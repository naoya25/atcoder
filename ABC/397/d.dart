import 'dart:io';
import 'dart:convert';
import 'dart:math';

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

  for (int i = 1; i <= calcCubeRootInt(n); ++i) {
    int j = calcCubeRootInt(n + i * i * i);
    if (j * j * j - i * i * i == n) {
      print('$j $i');
      return;
    }
  }

  print(-1);
}

int calcCubeRootInt(int t) {
  num cubeRoot = t >= 0 ? pow(t, 1 / 3) : -pow(-t, 1 / 3);
  int cubeRootInt = cubeRoot.round();
  return cubeRootInt;
}
