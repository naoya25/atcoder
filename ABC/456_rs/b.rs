use std::io::{self, Read};

struct Scanner {
    tokens: std::vec::IntoIter<String>,
}

impl Scanner {
    fn new() -> Self {
        let mut buffer = String::new();
        io::stdin().read_to_string(&mut buffer).expect("Read error");
        let tokens: Vec<String> = buffer.split_whitespace().map(|s| s.to_string()).collect();
        Self {
            tokens: tokens.into_iter(),
        }
    }

    fn next<T: std::str::FromStr>(&mut self) -> T {
        self.tokens
            .next()
            .expect("No more tokens")
            .parse()
            .ok()
            .expect("Parse error")
    }

    fn next_vec<T: std::str::FromStr>(&mut self, n: usize) -> Vec<T> {
        (0..n).map(|_| self.next()).collect()
    }
}

fn main() {
    let mut sc = Scanner::new();

    let a1: Vec<usize> = sc.next_vec::<usize>(6);
    let a2: Vec<usize> = sc.next_vec::<usize>(6);
    let a3: Vec<usize> = sc.next_vec::<usize>(6);

    let mut cnt = 0;

    for i in 0..6 {
        for j in 0..6 {
            for k in 0..6 {
                let dices = [a1[i], a2[j], a3[k]];
                if dices.contains(&4) && dices.contains(&5) && dices.contains(&6) {
                    cnt += 1;
                }
            }
        }
    }

    let total_cases = 6 * 6 * 6;
    println!("{}", cnt as f64 / total_cases as f64);
}
