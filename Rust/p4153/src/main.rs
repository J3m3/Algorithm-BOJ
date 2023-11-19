use std::fmt::Write;
use std::io::{stdin, Read};

fn main() {
    let mut buf = String::new();
    stdin().read_to_string(&mut buf).unwrap();
    let triangles: Vec<[usize; 3]> = buf
        .lines()
        .map(|line| {
            line.split_ascii_whitespace()
                .map(|c| c.parse().unwrap())
                .collect::<Vec<usize>>()
                .try_into()
                .unwrap()
        })
        .collect();

    let mut output = String::new();
    for triangle in triangles {
        let [a, b, c] = triangle;
        if let (0, 0, 0) = (a, b, c) {
            break;
        }
        let is_right = a * a + b * b == c * c || a * a + c * c == b * b || b * b + c * c == a * a;
        if is_right {
            writeln!(output, "right").unwrap();
        } else {
            writeln!(output, "wrong").unwrap();
        }
    }
    println!("{output}");
}
