use std::collections::VecDeque;
use std::io::{stdin, Read};

static MOVES: [(i32, i32); 4] = [(1, 0), (0, 1), (-1, 0), (0, -1)];

fn main() {
    let mut buf = String::new();
    stdin().read_to_string(&mut buf).unwrap();
    let board: Vec<Vec<u8>> = buf
        .trim_end()
        .split('\n')
        .skip(1)
        .map(|s| s.into())
        .collect();
    let h = board.len();
    let w = board[0].len();
    let (x, y) = board
        .iter()
        .enumerate()
        .map(|en| {
            let (y, ref s) = (en.0, en.1);
            match s.iter().position(|&val| val == 'I' as u8) {
                Some(x) => Some((x, y)),
                None => None,
            }
        })
        .find(|val| val.is_some())
        .flatten()
        .unwrap();

    let mut answer = 0;
    let mut visited: Vec<Vec<bool>> = vec![vec![false; w]; h];
    let mut queue = VecDeque::from([(x, y)]);

    while let Some((x, y)) = queue.pop_front() {
        for (dx, dy) in MOVES {
            let nx = x as i32 + dx;
            let ny = y as i32 + dy;

            if nx < 0 || nx >= w as i32 || ny < 0 || ny >= h as i32 {
                continue;
            }
            let nx = nx as usize;
            let ny = ny as usize;
            if visited[ny][nx] {
                continue;
            }
            if board[ny][nx] == 'X' as u8 {
                continue;
            }

            if board[ny][nx] == 'P' as u8 {
                answer += 1;
            }
            visited[ny][nx] = true;
            queue.push_back((nx, ny));
        }
    }

    println!(
        "{}",
        if answer == 0 {
            String::from("TT")
        } else {
            answer.to_string()
        }
    );
}
