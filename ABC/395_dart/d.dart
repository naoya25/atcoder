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

/// ===================================
/// 鳩と巣の関係を管理するデータ構造
/// 共通して 0-index で管理
/// 鳩の移動 と 巣にいる鳩の一括移動を高速に行う
///
/// ロジック
/// 仮想的な「ラベル鳩」を用意して、鳩の移動と巣の情報を管理する
/// 1. 鳩 i を巣 j に移動
///   鳩 i を、ラベル鳩 j が入っている巣に移動させる。
/// 2. 巣 i の鳩を巣 j に移動
///   ラベル鳩 i と j の巣を入れ替える。
/// 3. 鳩の巣の計算
///   鳩 i が入っている巣に付いているラベル鳩の番号を計算する。
/// ===================================

class PigeonNestSystem {
  List<int> nestToLabel; // 各巣のラベル鳩
  List<int> labelToNest; // 各ラベル鳩の巣
  List<int> pigeonToNest; // 各鳩の巣

  PigeonNestSystem(int n)
    : nestToLabel = List<int>.generate(n, (i) => i),
      labelToNest = List<int>.generate(n, (i) => i),
      pigeonToNest = List<int>.generate(n, (i) => i);

  /// 鳩 (pigeon) が巣 (nest) に移動
  void movePigeon(int pigeon, int nest) {
    pigeonToNest[pigeon] = labelToNest[nest];
  }

  /// 巣(beforeNest) にいる鳩が巣(afterNest) に移動
  void moveNestPigeons(int beforeNest, int afterNest) {
    int tmp = labelToNest[beforeNest];
    labelToNest[beforeNest] = labelToNest[afterNest];
    labelToNest[afterNest] = tmp;

    int index0 = labelToNest[beforeNest];
    int index1 = labelToNest[afterNest];
    tmp = nestToLabel[index0];
    nestToLabel[index0] = nestToLabel[index1];
    nestToLabel[index1] = tmp;
  }

  /// 鳩 (pigeon) が入っている巣を計算
  int getPigeonNest(int pigeon) {
    return nestToLabel[pigeonToNest[pigeon]];
  }
}

void main() {
  final input = Input();
  final [N, Q] = input.getInts(2);

  final pigeonSys = PigeonNestSystem(N);

  for (int i = 0; i < Q; ++i) {
    final type = input.getInt();

    if (type == 1) {
      final [a, b] = input.getInts0idx(2);
      pigeonSys.movePigeon(a, b);
    } else if (type == 2) {
      final [a, b] = input.getInts0idx(2);
      pigeonSys.moveNestPigeons(a, b);
    } else {
      final a = input.getInt0idx();
      print(pigeonSys.getPigeonNest(a) + 1);
    }
  }
}
