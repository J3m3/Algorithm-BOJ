use std::fmt::Write;
use std::io::{stdin, Read};

fn check(board: &Vec<Vec<usize>>, lu: (usize, usize), range: usize) -> Option<usize> {
    let capacity = range * range;
    let mut blue = 0;
    let mut white = 0;
    for y in lu.1..lu.1 + range {
        for x in lu.0..lu.0 + range {
            if board[y][x] == 0 {
                white += 1;
            } else {
                blue += 1;
            }
        }
    }
    if blue == capacity {
        Some(1)
    } else if white == capacity {
        Some(0)
    } else {
        None
    }
}

fn solve(
    board: &Vec<Vec<usize>>,
    n_white: &mut usize,
    n_blue: &mut usize,
    lu: (usize, usize),
    range: usize,
) {
    if range == 0 {
        return;
    }

    match check(board, lu, range) {
        Some(color) => {
            if color == 0 {
                *n_white += 1;
            } else {
                *n_blue += 1;
            }
        }
        None => {
            let next_range = range / 2;
            for quadrant in 1..=4 {
                let (x, y) = match quadrant {
                    1 => (lu.0 + next_range, lu.1),
                    2 => lu,
                    3 => (lu.0 + next_range, lu.1 + next_range),
                    4 => (lu.0, lu.1 + next_range),
                    _ => break,
                };
                solve(board, n_white, n_blue, (x, y), next_range);
            }
        }
    }
}

fn main() {
    let mut input = String::new();
    stdin().read_to_string(&mut input).unwrap();
    let board: Vec<Vec<usize>> = input
        .trim_end()
        .lines()
        .skip(1)
        .map(|line| {
            line.split_ascii_whitespace()
                .map(|c| c.parse().unwrap())
                .collect()
        })
        .collect();

    let mut n_white = 0;
    let mut n_blue = 0;
    solve(&board, &mut n_white, &mut n_blue, (0, 0), board.len());

    let mut output = String::new();
    writeln!(output, "{n_white}").unwrap();
    writeln!(output, "{n_blue}").unwrap();
    println!("{output}");
}
