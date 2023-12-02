use std::io::*;

fn calc_pref(pref: &Vec<Vec<i32>>, x1: usize, y1: usize, x2: usize, y2: usize) -> i32 {
    pref[x2][y2] + pref[x1 - 1][y1 - 1] - pref[x2][y1 - 1] - pref[x1 - 1][y2]
}

fn apply_pref(board: &Vec<Vec<char>>, pref: &mut Vec<Vec<i32>>, n: usize, m: usize) {
    for y in 1..n + 1 {
        for x in 1..m + 1 {
            let calculate = |t| t + pref[y - 1][x] + pref[y][x - 1] - pref[y - 1][x - 1];
            pref[y][x] = if y + x & 1 == 0 {
                match board[y - 1][x - 1] {
                    'B' => calculate(1),
                    'W' => calculate(0),
                    _ => unreachable!(),
                }
            } else {
                match board[y - 1][x - 1] {
                    'B' => calculate(0),
                    'W' => calculate(1),
                    _ => unreachable!(),
                }
            };
        }
    }
}

fn main() {
    let stdin = read_to_string(stdin().lock()).unwrap();
    let mut input = stdin.split_ascii_whitespace();
    let mut next = || input.next().unwrap().parse::<usize>().unwrap();

    let n = next();
    let m = next();
    let k = next();

    let board: Vec<Vec<char>> = input.map(|line| line.chars().collect()).collect();
    let mut pref: Vec<Vec<i32>> = vec![vec![0; m + 1]; n + 1];

    apply_pref(&board, &mut pref, n, m);

    let mut min = i32::MAX;
    let mut max = i32::MIN;
    for i in 1..=n - k + 1 {
        for j in 1..=m - k + 1 {
            let (x1, y1) = (i, j);
            let (x2, y2) = (k + i - 1, k + j - 1);
            let result = calc_pref(&pref, x1, y1, x2, y2);
            min = min.min(result);
            max = max.max(result);
        }
    }

    let whole = (k * k) as i32;
    println!(
        "{}",
        vec![min, max, whole - min, whole - max]
            .iter()
            .min()
            .unwrap()
    );
}
