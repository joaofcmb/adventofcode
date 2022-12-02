fn main() {
  let input = std::fs::read_to_string("inputs/day01.txt")
    .expect("Error reading input!");

  let input_lines: Vec<&str> = input.lines().collect();

  let lines_grouped_by_elf = input_lines
    .split(|line| line.is_empty());

  let mut total_calories_per_elf: Vec<i32> = lines_grouped_by_elf
    .map(|lines| {
      lines.iter()
      .map(|line| line.parse::<i32>().unwrap())
      .sum()
    }).collect();

  total_calories_per_elf.sort_by(|a, b| b.cmp(a));

  let sum_total_calories_top_three_elves: i32 = total_calories_per_elf.iter().take(3).sum();
  println!("{sum_total_calories_top_three_elves}");
}
