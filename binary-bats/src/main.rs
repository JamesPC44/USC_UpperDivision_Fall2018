use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let mut input: Vec<i32> = stdin
                            .lock()
                            .lines()
                            .next()
                            .unwrap()
                            .unwrap()
                            .chars()
                            .map(|ch| match ch { '0' => 0, '1' => 1, _ => panic!() })
                            .collect();

    let mut idxs = vec![];

    for i in 0..input.len() {
        if input[i] == 1 && i != 0 {
            idxs.push(i);
            let mut j = i;
            loop {
                if j >= input.len() { break; }
                input[j] ^= 1;
                j += i;
            }
        }
    }

    println!("{}", idxs.len());
}
