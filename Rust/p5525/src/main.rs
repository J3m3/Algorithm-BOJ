use std::io::{stdin, Read};

enum PatternCase {
    DoubleO,
    DoubleI,
    Matched,
}

fn is_pattern_matched(prev: char, curr: char) -> PatternCase {
    if prev == 'I' {
        PatternCase::DoubleI
    } else {
        if prev == curr {
            PatternCase::DoubleO
        } else {
            PatternCase::Matched
        }
    }
}

fn main() {
    let mut buf = String::new();
    stdin().read_to_string(&mut buf).unwrap();
    let mut buf = buf.split_ascii_whitespace();

    let pattern_type: usize = buf.next().unwrap().parse().unwrap();
    let m: usize = buf.next().unwrap().parse().unwrap();
    let sequence: Vec<_> = buf.next().unwrap().chars().collect();

    let i_idx = sequence.iter().position(|&c| c == 'I').unwrap_or(m);
    let mut prev_idx = i_idx + 1;
    let mut curr_idx = i_idx + 2;
    let mut match_count = 0;
    let mut match_counts: Vec<usize> = vec![];

    while curr_idx < m {
        let prev = sequence[prev_idx];
        let curr = sequence[curr_idx];
        match is_pattern_matched(prev, curr) {
            PatternCase::DoubleI => {
                match_counts.push(match_count);
                match_count = 0;

                prev_idx += 1;
                curr_idx += 1;
            }
            PatternCase::DoubleO => {
                match_counts.push(match_count);
                match_count = 0;

                let new_i_idx = sequence
                    .iter()
                    .skip(curr_idx + 1)
                    .position(|&c| c == 'I')
                    .unwrap_or(m);
                let new_i_idx = new_i_idx + curr_idx + 1;

                prev_idx = new_i_idx + 1;
                curr_idx = new_i_idx + 2;
            }
            PatternCase::Matched => {
                match_count += 1;

                prev_idx += 2;
                curr_idx += 2;
            }
        }
    }

    match_counts.push(match_count);
    let answer: usize = match_counts
        .iter()
        .map(|&count| {
            if count < pattern_type {
                0
            } else {
                count - pattern_type + 1
            }
        })
        .sum();
    println!("{answer}");
}
