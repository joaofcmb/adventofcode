use std::str::FromStr;

enum Play {
  Rock,
  Paper,
  Scissors,
}

enum RoundResult {
  Win,
  Lose,
  Draw,
}

impl FromStr for Play {
  type Err = String;

  fn from_str(s: &str) -> Result<Self, Self::Err> {
    match s {
        "A" | "X" => Ok(Play::Rock),
        "B" | "Y" => Ok(Play::Paper),
        "C" | "Z" => Ok(Play::Scissors),
        _ => Err(format!("Invalid play value: '{s}'"))
    }
}
}

impl FromStr for RoundResult {
  type Err = String;

  fn from_str(s: &str) -> Result<Self, Self::Err> {
      match s {
          "X" => Ok(RoundResult::Lose),
          "Y" => Ok(RoundResult::Draw),
          "Z" => Ok(RoundResult::Win),
          _ => Err(format!("Invalid play value: '{s}'"))
      }
  }
}

impl Play {
  fn value(&self) -> i32 {
    match *self {
      Play::Rock => 1,
      Play::Paper => 2,
      Play::Scissors => 3, 
    }
  }

  fn value_against(&self, opponent: &Play) -> i32 {
    match (self, opponent) {
        (Play::Rock, Play::Rock) | (Play::Paper, Play::Paper) | (Play::Scissors, Play::Scissors) => 3 + self.value(),
        (Play::Rock, Play::Scissors) | (Play::Paper, Play::Rock) | (Play::Scissors, Play::Paper) => 6 + self.value(),
        (Play::Rock, Play::Paper) | (Play::Paper, Play::Scissors) | (Play::Scissors, Play::Rock) => self.value(),
  }
}
}

impl RoundResult {
  fn value(&self) -> i32 {
    match self {
        RoundResult::Win => 6,
        RoundResult::Draw => 3,
        RoundResult::Lose => 0,
    }
  }

  fn value_against(&self, opponent: &Play) -> i32 {
    let self_play = match (self, opponent) {
        (RoundResult::Draw, opponent) => opponent,
        (RoundResult::Lose, Play::Paper) | (RoundResult::Win, Play::Scissors) => &Play::Rock,
        (RoundResult::Lose, Play::Scissors) | (RoundResult::Win, Play::Rock) => &Play::Paper,
        (RoundResult::Lose, Play::Rock) | (RoundResult::Win, Play::Paper) => &Play::Scissors,
    };

    self.value() + self_play.value()
  }
}

fn part1(input: &String) -> i32 {
  let strategy: Vec<(Play, Play)> = input.lines().into_iter()
    .map(|line| line.split_once(' ').unwrap())
    .map(|(opponent_play, your_play)| (Play::from_str(opponent_play).unwrap(), Play::from_str(your_play).unwrap()))
    .collect();

  strategy.into_iter()
    .map(|(opponent_play, your_play)| your_play.value_against(&opponent_play))
    .sum()
}

fn part2(input: &String) -> i32 {
  let strategy: Vec<(Play, RoundResult)> = input.lines().into_iter()
    .map(|line| line.split_once(' ').unwrap())
    .map(|(opponent_play, your_play)| (Play::from_str(opponent_play).unwrap(), RoundResult::from_str(your_play).unwrap()))
    .collect();

  strategy.into_iter()
    .map(|(opponent_play, desired_result)| desired_result.value_against(&opponent_play))
    .sum()
}

fn main() {
  let input = std::fs::read_to_string("inputs/day02.txt")
    .expect("Error reading input!");

  println!("{}", part1(&input));
  println!("{}", part2(&input));
}
