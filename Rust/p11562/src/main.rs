use std::fmt::Write;
use std::io::*;

fn floyd_warshall(board: &mut Vec<Vec<i32>>, n: usize) {
    for via in 0..n {
        for u in 0..n {
            for v in 0..n {
                let dist = board[u][via] + board[via][v];
                if board[u][v] > dist {
                    board[u][v] = dist;
                }
            }
        }
    }
}

fn main() {
    let stdin = read_to_string(stdin().lock()).unwrap();
    let mut input = stdin.split_ascii_whitespace();
    let mut next = || input.next().unwrap().parse::<usize>().unwrap();

    let n = next();
    let m = next();

    let mut board: Vec<Vec<i32>> = (0..n)
        .map(|_| vec![0; n])
        .enumerate()
        .map(|(y, v)| {
            v.iter()
                .enumerate()
                .map(|(x, _)| if x == y { 0 } else { 10e8 as i32 })
                .collect()
        })
        .collect();

    for _ in 0..m {
        let u = next() - 1;
        let v = next() - 1;
        let b = next();

        board[u][v] = 0;
        if b == 1 {
            board[v][u] = 0;
        } else {
            board[v][u] = 1;
        }
    }
    floyd_warshall(&mut board, n);

    let mut output = String::new();
    let k = next();
    for _ in 0..k {
        let s = next() - 1;
        let e = next() - 1;
        writeln!(output, "{}", board[s][e]).ok();
    }
    println!("{output}");
}
