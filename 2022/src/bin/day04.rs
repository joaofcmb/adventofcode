use std::str::FromStr;

struct Range {
  lower: u32,
  upper: u32,
}

impl Range {
  fn contains(&self, other: &Range) -> bool {
    let range = self.lower..=self.upper;
    range.contains(&other.lower) && range.contains(&other.upper)
  }

  fn overlaps(&self, other: &Range) -> bool {
    self.lower <= other.upper && other.lower <= self.upper
  }
}

impl FromStr for Range {
    type Err = std::num::ParseIntError;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let mut split_s = s.split('-');

        let lower = split_s.next().unwrap().parse::<u32>().unwrap();
        let upper = split_s.next().unwrap().parse::<u32>().unwrap();

        Ok(Range { lower, upper })
    }
}

fn part1(input: &String) -> usize {
  input.lines().into_iter()
    .map(|line| line.split(',').take(2).collect::<Vec<&str>>())
    .map(|line_ranges| (Range::from_str(line_ranges[0]).unwrap(), Range::from_str(line_ranges[1]).unwrap()))
    .filter(|(r1, r2)| r1.contains(r2) || r2.contains(r1))
    .count()
}

fn part2(input: &String) -> usize {
  input.lines().into_iter()
    .map(|line| line.split(',').take(2).collect::<Vec<&str>>())
    .map(|line_ranges| (Range::from_str(line_ranges[0]).unwrap(), Range::from_str(line_ranges[1]).unwrap()))
    .filter(|(r1, r2)| r1.overlaps(r2))
    .count()
}

fn main() {
  let input = std::fs::read_to_string("inputs/day04.txt")
    .expect("Error reading input!");

  println!("{}", part1(&input));
  println!("{}", part2(&input));
}
