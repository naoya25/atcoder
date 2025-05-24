import 'dart:io';
import 'dart:convert';

void main() {
  final input = _Input();
  final [n, m, q] = input.getInts(3);

  Map<int, Set<int>> userEnabledPages = {};
  for (int i = 1; i <= n; ++i) {
    userEnabledPages[i] = {};
  }
  Set<int> allEnabledUsers = {};

  for (int i = 0; i < q; ++i) {
    int qt = input.getInt();
    if (qt == 1) {
      final [x, y] = input.getInts(2);
      userEnabledPages[x]!.add(y);
    } else if (qt == 2) {
      int x = input.getInt();
      allEnabledUsers.add(x);
    } else if (qt == 3) {
      final [x, y] = input.getInts(2);
      if (allEnabledUsers.contains(x) || userEnabledPages[x]!.contains(y)) {
        print('Yes');
      } else {
        print('No');
      }
    }
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
