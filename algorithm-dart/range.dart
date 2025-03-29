RangeIterable range(int from, [int? to, int? step]) =>
    RangeIterable(from, to, step);

class RangeIterable extends Iterable<int> {
  RangeIterable(int from, [int? to, int? step])
    : iterator = RangeIterator(from, to, step),
      super();

  @override
  final RangeIterator iterator;
}

class RangeIterator implements Iterator<int> {
  RangeIterator(int n, [int? m, int? s])
    : from = m == null ? 0 : n,
      to = m == null ? n : m,
      step = s ?? 1,
      current = (m == null ? 0 : n) - (s ?? 1);

  final int from;
  final int to;
  final int step;

  @override
  late int current;

  @override
  bool moveNext() {
    current += step;
    if (step > 0 && current >= to) return false;
    if (step < 0 && current <= to) return false;
    return true;
  }
}
