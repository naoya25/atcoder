import 'dart:io';
import 'dart:convert';

void main() {
  final input = Input();
  int n = input.getInt();
  List<String> s = input.getStrings(n);
  s.sortByLenAsc();

  printList(s, separator: "");
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

void printList(List<String> list, {String separator = ' '}) {
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

extension StringList on List<String> {
  void sortAsc() => sort((a, b) => a.compareTo(b));
  void sortDesc() => sort((a, b) => b.compareTo(a));
  void sortByLenAsc() => sort((a, b) => a.length.compareTo(b.length));
  void sortByLenDesc() => sort((a, b) => b.length.compareTo(a.length));
}
