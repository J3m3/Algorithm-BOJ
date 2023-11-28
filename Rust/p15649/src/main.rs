use std::fmt::Write;
use std::io::{stdin, Read};

static mut N: usize = 0;
static mut M: usize = 0;

unsafe fn dfs(result: &mut Vec<usize>, visited: &mut Vec<bool>, output: &mut impl Write) {
    if result.len() == M {
        let answer: Vec<_> = result.iter().map(|&c| c.to_string()).collect();
        writeln!(output, "{}", answer.join(" ")).unwrap();
        return;
    }
    for i in 1..N + 1 {
        if !visited[i] {
            result.push(i);
            visited[i] = true;
            dfs(result, visited, output);
            result.pop();
            visited[i] = false;
        }
    }
}

fn main() {
    let mut buf = String::new();
    stdin().read_to_string(&mut buf).unwrap();

    let mut buf = buf.split_ascii_whitespace().flat_map(str::parse::<usize>);
    unsafe { N = buf.next().unwrap() };
    unsafe { M = buf.next().unwrap() };
    let mut result: Vec<usize> = vec![];
    let mut visited = vec![false; unsafe { N + 1 }];
    let mut output = String::new();

    unsafe { dfs(&mut result, &mut visited, &mut output) };

    println!("{output}");
}
