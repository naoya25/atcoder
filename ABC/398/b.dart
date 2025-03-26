import 'dart:io';

void main() {
  List<int> a = stdin.readLineSync()!.split(' ').map(int.parse).toList();
  List<int> counter = List.filled(14, 0);

  for (int i = 0; i < a.length; i++) {
    counter[a[i]]++;
  }

  counter.sort((a, b) => b.compareTo(a));

  if (counter[0] >= 3 && counter[1] >= 2) {
    print('Yes');
  } else {
    print('No');
  }
}
