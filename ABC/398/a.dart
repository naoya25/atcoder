import 'dart:io';

void main() {
  int n = int.parse(stdin.readLineSync()!);
  bool isEven = n % 2 == 0;
  String ans = '';

  if (isEven) {
    n = (n - 2) ~/ 2;
  } else {
    n = (n - 1) ~/ 2;
  }

  ans += '-' * n;
  ans += '=' * (isEven ? 2 : 1);
  ans += '-' * n;

  print(ans);
}
