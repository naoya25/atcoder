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
  final [n, r, c] = input.getInts(3);
  String s = input.getString();
  /*
  煙を移動させると全ての煙の座標を更新しなければいけない
  だから煙は移動させず、userと煙発生源が相対的に移動したと考える
  */

  Point userPoint = Point(r, c); // ユーザーの位置
  Point smokePoint = Point(0, 0); // 煙発生源
  Set<Point> smokes = {Point(0, 0)};
  String ans = '';

  for (int i = 0; i < n; ++i) {
    if (s[i] == 'S') {
      smokePoint.x--;
      userPoint.x--;
    } else if (s[i] == 'N') {
      smokePoint.x++;
      userPoint.x++;
    } else if (s[i] == 'E') {
      smokePoint.y--;
      userPoint.y--;
    } else if (s[i] == 'W') {
      smokePoint.y++;
      userPoint.y++;
    }
    smokes.add(Point(smokePoint.x, smokePoint.y));

    if (smokes.contains(userPoint)) {
      ans += '1';
    } else {
      ans += '0';
    }
  }

  print(ans);
}
