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
}

fn main() {
    let mut sc = Scanner::new();

    let n: usize = sc.next();

    if 3 <= n && n <= 18 {
        println!("Yes");
    } else {
        println!("No");
    }
}
