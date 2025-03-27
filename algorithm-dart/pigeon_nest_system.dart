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
