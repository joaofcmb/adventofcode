fn part1(mut stacks: Vec<Vec<char>>, moves: &Vec<(usize, usize, usize)>) -> String {
  for (n_moves, from, to) in moves {
    for _ in 0..*n_moves {
      let value = stacks[*from].pop().unwrap();
      stacks[*to].push(value);
    }
  }

  stacks.into_iter()
    .map(|stack| stack.last().unwrap().to_owned())
    .collect::<String>()
}

fn part2(mut stacks: Vec<Vec<char>>, moves: &Vec<(usize, usize, usize)>) -> String {
  for (n_moves, from, to) in moves {
    let n_moves_to_len = stacks[*from].len() - n_moves;
    let mut values = stacks[*from].split_off(n_moves_to_len);
    stacks[*to].append(&mut values);
  }

  stacks.into_iter()
    .map(|stack| stack.last().unwrap().to_owned())
    .collect::<String>()
}

fn main() {
  let input = std::fs::read_to_string("inputs/day05.txt")
    .expect("Error reading input!");

  let input_lines: Vec<&str> = input.lines().collect();

  let mut split_input_lines = input_lines.split(|&line| line.is_empty());

  let mut stacks_lines: Vec<&str> = split_input_lines.next().unwrap().to_vec();

  stacks_lines.pop();
  stacks_lines.reverse();

  let mut stacks_transposed_iters: Vec<_>  = stacks_lines.into_iter()
    .map(|line| {
      line.chars().collect::<Vec<char>>()
        .chunks(4)
        .map(|chunk| chunk[1])
        .collect::<Vec<char>>()
        .into_iter()
    }).collect();

  let stacks: Vec<Vec<char>> = (0..stacks_transposed_iters[0].len())
    .map(|_| {
      stacks_transposed_iters.iter_mut()
        .map(|stack_transposed_iter| stack_transposed_iter.next().unwrap())
        .filter(|item| !item.is_whitespace())
        .collect::<Vec<char>>()
    }).collect();

  let moves: Vec<(usize, usize, usize)> = split_input_lines.next().unwrap().into_iter()
    .map(|m| m.split_whitespace().flat_map(|token| token.parse::<usize>()))
    .map(|mut numbers| (numbers.next().unwrap(), numbers.next().unwrap() - 1, numbers.next().unwrap() - 1))
    .collect();

  println!("{}", part1(stacks.clone(), &moves));
  println!("{}", part2(stacks, &moves));
}
