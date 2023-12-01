use std::fmt::Write;
use std::io::*;

fn apply_prefix(board: &Vec<Vec<i32>>, pref: &mut Vec<Vec<i32>>, n: usize) {
    for y in 1..n + 1 {
        for x in 1..n + 1 {
            pref[y][x] = pref[y][x - 1] + board[y][x];
        }
    }
    for x in 1..n + 1 {
        for y in 1..n + 1 {
            pref[y][x] = pref[y - 1][x] + pref[y][x];
        }
    }
}

fn main() {
    let stdin = read_to_string(stdin().lock()).unwrap();
    let mut input = stdin.split_ascii_whitespace();
    let mut next = || input.next().unwrap().parse::<usize>().unwrap();

    let n = next();
    let m = next();

    let mut board: Vec<Vec<i32>> = vec![vec![0; n + 1]; n + 1];
    let mut pref = board.clone();
    for i in 1..n + 1 {
        for j in 1..n + 1 {
            board[i][j] = next() as i32;
        }
    }

    apply_prefix(&board, &mut pref, n);

    let mut output = String::new();
    for _ in 0..m {
        let x1 = next();
        let y1 = next();
        let x2 = next();
        let y2 = next();

        let answer = pref[x2][y2] - pref[x2][y1 - 1] - pref[x1 - 1][y2] + pref[x1 - 1][y1 - 1];
        writeln!(output, "{answer}").ok();
    }
    println!("{output}");
}
