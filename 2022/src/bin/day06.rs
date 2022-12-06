use std::{iter::zip, collections::HashSet};

fn part1(input: &String) -> usize {
  let chars: Vec<char> = input.chars().collect();

  zip(
    zip(&chars[0..], &chars[1..]),
    zip(&chars[2..],&chars[3..])
  ).position(|((a, b), (c, d))| {
    let mut unique_set = HashSet::new();
    [a, b, c, d].into_iter().all(|c| unique_set.insert(c))
  }).unwrap() + 4
}
  

fn part2(input: &String) -> usize {
  let chars: Vec<char> = input.chars().collect();

  (0..chars.len() - 14)
    .position(|i| {
      let mut unique_set = HashSet::new();
      chars[i..i+14].into_iter().all(|c| unique_set.insert(c))
    }).unwrap() + 14
}

fn main() {
  let input = std::fs::read_to_string("inputs/day06.txt")
    .expect("Error reading input!");
  

  println!("{}", part1(&input));
  println!("{}", part2(&input));
}
