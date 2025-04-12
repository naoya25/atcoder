import 'dart:io';
import 'dart:convert';

void main() {
  final input = _Input();
  final [n, k] = input.getInts(2);
  final String S = input.getString();

  String answer = solve(n, k, S);

  print(answer);
}

String solve(int N, int K, String S) {
  // dp[i][c][l]:
  //   Sの先頭i文字(0~i-1番目)をどう置いたかを考えたとき、
  //   '.' を c 個使用し、直前が '.'(l=1) か '0'(l=0) か、
  //   という割当が少なくとも1つ存在するなら true
  //
  //  配列のサイズ: (N+1) x (K+1) x 2
  //  ただし N,K が大きい場合は要メモリ注意
  List<List<List<bool>>> dp = List.generate(
    N + 1,
    (_) => List.generate(K + 1, (_) => List.filled(2, false)),
  );

  // 初期化: まだ何も置いてない段階 (i=0) で '.'を0個, 直前='0' 相当にtrue
  // 「直前が '.' だった」状況はないので false
  dp[0][0][0] = true;
  dp[0][0][1] = false;

  // 前向きDP
  for (int i = 0; i < N; i++) {
    for (int c = 0; c <= K; c++) {
      for (int l = 0; l < 2; l++) {
        if (!dp[i][c][l]) continue; // 到達不可ならスキップ
        final char = S[i];

        // 1) i番目を '0' として置けるか？
        //    S[i] が '0' または '?' なら可能
        //    次の状態は dp[i+1][c][0] = true
        if (char == 'o' || char == '?') {
          dp[i + 1][c][0] = true;
        }

        // 2) i番目を '.' として置けるか？
        //    S[i] が '.' または '?' なら可能
        //    ただし連続禁止なので「直前が '.'」ではNG → l=0 でないといけない
        //    '.' の数 c は増えるので c+1 <= K
        if ((char == '.' || char == '?') && l == 0 && c < K) {
          dp[i + 1][c + 1][1] = true;
        }
      }
    }
  }

  // 有効割当が存在するか確認 (問題によっては「存在しないときは～」等の処理が必要かも)
  bool possible = dp[N][K][0] || dp[N][K][1];
  if (!possible) {
    // X が空 (解がない) 場合の出力は問題文次第。ここでは一応空文字を返す例。
    return "";
  }

  // 逆向きに辿るための「後ろからの到達可能」フラグ
  // backward[i][c][l] = 「dp[i][c][l] が true で、そこから最終状態まで到達できるか？」
  List<List<List<bool>>> backward = List.generate(
    N + 1,
    (_) => List.generate(K + 1, (_) => List.filled(2, false)),
  );

  // ゴール (i=N, c=K, l=0 or 1) が true ならそこを到達可能にしてスタート
  if (dp[N][K][0]) backward[N][K][0] = true;
  if (dp[N][K][1]) backward[N][K][1] = true;

  // 各位置が '.' / '0' になり得るか
  List<bool> canDot = List.filled(N, false);
  List<bool> canZero = List.filled(N, false);

  // i を N-1 から 0 へ辿る
  for (int i = N; i > 0; i--) {
    // c, l を走査
    for (int c = 0; c <= K; c++) {
      for (int l = 0; l < 2; l++) {
        if (!backward[i][c][l]) continue; // 到達できないならスキップ

        // i-1番目をどう置いたかを逆算する。
        // 「dp[i-1][c'][l'] から i-1番目を X にして dp[i][c][l] に遷移した」なら
        // backward[i-1][c'][l'] = true にし、Xが '.' / '0' なら canDot[i-1] / canZero[i-1] = true

        final char = S[i - 1];

        // Case A: i-1 番目が '0' だった
        //   → dp[i-1][c][ any l'] から i-1を '0' にして dp[i][c][0] へ遷移
        //   → つまり l=0 のときは「直前に '.' は置いていない」ことになる
        //   → char が '0' or '?' なら '0' は置ける
        if (l == 0) {
          // i-1で '0' を置く → c は増えないので c' = c
          //   前の l' は 0 でも 1 でもよい (どちらからでも '0' を置ける)
          if (char == 'o' || char == '?') {
            for (int lPrev = 0; lPrev < 2; lPrev++) {
              if (dp[i - 1][c][lPrev]) {
                backward[i - 1][c][lPrev] = true;
                canZero[i - 1] = true;
              }
            }
          }
        }

        // Case B: i-1 番目が '.'
        //   → dp[i-1][c-1][0] から i-1を '.' にして dp[i][c][1]
        //   → 連続禁止なので「直前が '.' 」= l'=1 はダメ → l'は0
        //   → '.' を1つ増やすので c' = c-1
        if (l == 1) {
          // c-1 >= 0
          int cPrev = c - 1;
          if (cPrev >= 0) {
            if (char == '.' || char == '?') {
              // i-1で '.' を置くには dp[i-1][c-1][0] が true である必要
              if (dp[i - 1][cPrev][0]) {
                backward[i - 1][cPrev][0] = true;
                canDot[i - 1] = true;
              }
            }
          }
        }
      }
    }
  }

  // 最後に各位置ごとに T_i を決定
  List<String> result = List.filled(N, '?');
  for (int i = 0; i < N; i++) {
    // 「canDot[i] == true, canZero[i] == false」なら T_i='.'
    if (canDot[i] && !canZero[i]) {
      result[i] = '.';
    }
    // 「canDot[i] == false, canZero[i] == true」なら T_i='0'
    else if (!canDot[i] && canZero[i]) {
      result[i] = 'o';
    }
    // 両方 true or 両方 false(本来あり得ないが) → '?'
    else {
      result[i] = '?';
    }
  }

  return result.join('');
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
