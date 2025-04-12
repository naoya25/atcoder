import 'dart:io';
import 'dart:convert';

void main() {
  final input = Input();
  final [n, k] = input.getInts(2);

  int m = 1000000000;

  List<int> a = List.filled(n + 1, 0);
  List<int> prefixSum = List.filled(n + 1, 0);

  for (int i = 0; i <= n; i++) {
    if (i < k) {
      a[i] = 1;
    } else {
      a[i] = prefixSum[i - 1] - (i - k - 1 >= 0 ? prefixSum[i - k - 1] : 0);
      a[i] %= m;
    }
    prefixSum[i] = ((i > 0 ? prefixSum[i - 1] : 0) + a[i]) % m;
  }

  print(a[n] % m);
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
