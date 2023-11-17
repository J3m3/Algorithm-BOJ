use std::fmt::Write;
use std::io::{stdin, Read};

fn is_palindrome(nums: &[u8], start_idx: usize, end_idx: usize) -> bool {
    if start_idx >= end_idx {
        return true;
    }
    if nums[start_idx] == nums[end_idx] {
        is_palindrome(nums, start_idx + 1, end_idx - 1)
    } else {
        false
    }
}

fn main() {
    let mut input = String::new();
    stdin().read_to_string(&mut input).unwrap();
    let input = input.split_ascii_whitespace();

    let mut output = String::new();
    for num_str in input {
        if num_str == "0" {
            break;
        };

        let nums = num_str.trim_start_matches('0').as_bytes();
        let result = is_palindrome(nums, 0, nums.len() - 1);
        if result {
            writeln!(output, "yes").unwrap();
        } else {
            writeln!(output, "no").unwrap();
        }
    }
    println!("{output}");
}
