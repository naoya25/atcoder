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

  for (int d = 1; d * d * d <= n; ++d) {
    if (n % d != 0) continue;

    int m = n ~/ d;
    int k = sol(3, 3 * d, d * d - m);

    if (k > 0) {
      print('${k + d} $k');
      return;
    }
  }

  print(-1);
}

int sol(int a, int b, int c) {
  int l = 0, r = 600000001;
  while (r - l > 1) {
    int mid = (l + r) ~/ 2;
    if (a * mid * mid + b * mid + c <= 0)
      l = mid;
    else
      r = mid;
  }
  if (a * l * l + b * l + c == 0) return l;
  return -1;
}
