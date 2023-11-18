use std::collections::VecDeque;
use std::fmt::Write;
use std::io::{stdin, Read};

static MOVES: [(i32, i32); 4] = [(1, 0), (0, 1), (-1, 0), (0, -1)];

fn solve(board: &Vec<Vec<i32>>) -> Vec<Vec<i32>> {
    let y_len = board.len();
    let x_len = board[0].len();
    let mut result_board: Vec<Vec<i32>> = vec![vec![-1; x_len]; y_len];
    let mut visited: Vec<Vec<bool>> = vec![vec![false; x_len]; y_len];

    let start_point = board.iter().flatten().position(|&val| val == 2).unwrap();
    let (sx, sy) = (start_point % x_len, start_point / x_len);

    let mut queue: VecDeque<(usize, usize, usize)> = VecDeque::from([(0, sx, sy)]);
    result_board[sy][sx] = 0;
    visited[sy][sx] = true;

    while let Some((step, x, y)) = queue.pop_front() {
        for (dx, dy) in MOVES {
            let nx = (x as i32) + dx;
            let ny = (y as i32) + dy;

            if nx < 0 || ny < 0 || nx >= x_len as i32 || ny >= y_len as i32 {
                continue;
            }
            let nx: usize = nx.try_into().unwrap();
            let ny: usize = ny.try_into().unwrap();
            if board[ny][nx] == 0 || visited[ny][nx] {
                continue;
            }
            let step = step + 1;
            queue.push_back((step, nx, ny));
            visited[ny][nx] = true;
            result_board[ny][nx] = step as i32;
        }
    }
    for y in 0..y_len {
        for x in 0..x_len {
            if board[y][x] == 0 {
                result_board[y][x] = 0;
            }
        }
    }
    result_board
}

fn main() {
    let mut buf = String::new();
    stdin().read_to_string(&mut buf).unwrap();
    let board: Vec<Vec<i32>> = buf
        .trim_end()
        .lines()
        .skip(1)
        .map(|line| {
            line.split_ascii_whitespace()
                .map(|c| c.parse().unwrap())
                .collect()
        })
        .collect();

    let result_board: Vec<Vec<i32>> = solve(&board);

    let mut output = String::new();
    for row in result_board {
        let result = row
            .iter()
            .map(|x| x.to_string())
            .collect::<Vec<String>>()
            .join(" ");
        writeln!(output, "{result}").unwrap();
    }
    println!("{output}");
}
