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
