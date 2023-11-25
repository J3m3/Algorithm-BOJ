use ::std::io::stdin;
use std::cmp::min;

fn main() {
    let mut buf = String::new();
    stdin().read_line(&mut buf).unwrap();
    let n: usize = buf.trim_end().parse().unwrap();
    let mut dp: Vec<_> = (0..n + 1).map(|_| 5).collect();
    dp[0] = 0;
    dp[1] = 1;

    for i in 2..n + 1 {
        let mut step = 1;
        let mut squared = 1;
        while squared <= i {
            dp[i] = min(dp[i], dp[i - squared] + 1);
            step += 1;
            squared = step * step;
        }
    }
    println!("{}", dp[n]);
}

// 26 = 1^2 + 5^2
// 26 = 1^2 + 4^2 + 3^2
// D[26] = min(D[26-25], D[26-16], D[26-9], D[26-1]) + 1
// D[26] = min(D[1], D[10], D[17], D[1]) + 1

// D[1] = 1
// D[2] = min(D[2-1]) + 1

// D[4] = min(D[4-1], D[4-2], D[4-4]) + 1
// D[4] = min(D[3], D[2], D[0]) + 1
