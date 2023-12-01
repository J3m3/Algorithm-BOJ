use std::fmt::Write;
use std::io::{stdin, Read};

fn solve(holds_list: &Vec<Vec<i32>>, n: usize) {
    let mut output = String::new();

    let mut pref = vec![0; n + 1];
    for vector in holds_list {
        for (i, &val) in vector.iter().enumerate() {
            pref[i + 1] = pref[i] + val;
        }

        let mut dp = vec![0; n + 1];
        for i in 1..n + 1 {
            let mut minimum = i32::MAX;
            for j in 0..i {
                minimum = minimum.min(pref[i] - pref[j] - dp[j]);
            }
            dp[i] = minimum;
        }

        let answer = match dp[n] {
            ..=-1 => "A",
            0 => "D",
            1.. => "B",
        };
        writeln!(output, "{answer}").unwrap();
    }
    println!("{output}");
}

fn main() {
    let mut buf = String::new();
    stdin().read_to_string(&mut buf).unwrap();
    let mut it = buf.trim_end().split('\n');

    let n: usize = it.next().unwrap().parse().unwrap();
    let holds_list: Vec<Vec<i32>> = it
        .map(|line| line.split_ascii_whitespace().flat_map(str::parse).collect())
        .collect();

    solve(&holds_list, n);
}
