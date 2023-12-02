use std::fmt::Write;
use std::io::*;

fn main() {
    let stdin = read_to_string(stdin().lock()).unwrap();
    let mut input = stdin.split_ascii_whitespace();
    let mut next = || input.next().unwrap().parse::<usize>().unwrap();
}

fn print_2dv<T: std::fmt::Debug>(v: &Vec<Vec<T>>) {
    v.iter().for_each(|v| println!("{:^3?}", v));
    println!();
}
