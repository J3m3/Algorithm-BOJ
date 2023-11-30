use std::{
    cmp::min,
    io::{stdin, Read},
};

fn calc_diff(team: &Vec<bool>, board: &Vec<Vec<usize>>, n: &usize) -> usize {
    let mut team_link_sum = 0;
    let mut team_start_sum = 0;
    for i in 0..*n {
        for j in i + 1..*n {
            if team[i] && team[j] {
                team_link_sum += board[i][j] + board[j][i];
            } else if !team[i] && !team[j] {
                team_start_sum += board[i][j] + board[j][i];
            }
        }
    }
    team_link_sum.abs_diff(team_start_sum)
}

fn solve(
    board: &Vec<Vec<usize>>,
    n: &usize,
    start: usize,
    depth: usize,
    team: &mut Vec<bool>,
    result: &mut usize,
) {
    if depth == *n / 2 {
        *result = min(*result, calc_diff(team, board, n));
        return;
    }
    for i in start..*n {
        team[i] = true;
        solve(board, n, i + 1, depth + 1, team, result);
        team[i] = false;
    }
}

fn main() {
    let mut buf = String::new();
    stdin().read_to_string(&mut buf).unwrap();
    let mut it = buf.trim_end().split('\n');

    let n = it.next().unwrap().parse().unwrap();
    let board: Vec<Vec<usize>> = it
        .map(|line| line.split_ascii_whitespace().flat_map(str::parse).collect())
        .collect();
    let mut result = std::usize::MAX;
    let mut team: Vec<bool> = vec![false; n];

    solve(&board, &n, 0, 0, &mut team, &mut result);

    println!("{result}");
}
