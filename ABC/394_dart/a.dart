import 'dart:io';
import 'dart:convert';

void main() {
  final input = Input();
  String s = input.getString();

  int cnt = 0;
  for (int i = 0; i < s.length; ++i) {
    if (s[i] == '2') {
      cnt++;
    }
  }
  print('2' * cnt);
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
}
