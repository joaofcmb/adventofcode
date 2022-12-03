use std::collections::HashSet;

fn common_char(strings: &[&str]) -> char {
  strings.into_iter()
    .map(|string| string.chars().collect::<HashSet<char>>())
    .reduce(|acc, charset| acc.intersection(&charset).copied().collect())
    .unwrap().into_iter()
    .next().unwrap()
}

fn priority(char: char) -> u32 {
  match char {
      'a'..='z' => char as u32 - 'a' as u32 + 1,
      'A'..='Z' => char as u32 - 'A' as u32 + 27,
      _ => 0
  }
}

fn part1(input: &String) -> u32 {
  input.lines().into_iter()
    .map(|line| line.split_at(line.len()/2))
    .map(|(half1, half2)| priority(common_char(&[half1, half2])))
    .sum()
}

fn part2(input: &String) -> u32 {
  input.lines().collect::<Vec<&str>>()
    .chunks(3)
    .map(|rucksacks| priority(common_char(rucksacks)))
    .sum()
}

fn main() {
  let input = std::fs::read_to_string("inputs/day03.txt")
    .expect("Error reading input!");

  println!("{}", part1(&input));
  println!("{}", part2(&input));
}
