use std::ops::Add;

#[derive(Debug)]
struct Cell {
  height: u32,
  visible: bool
}

impl Cell {
    fn scenic_score(&self, &row: &usize, &col: &usize, heightmap: &Vec<Vec<Cell>>) -> usize {
      let view_up = (0..row).rev()
        .take_while(|&i| heightmap[i][col].height < self.height)
        .collect::<Vec<_>>()
        .len()
        .add(1)
        .min(row);
      
      let view_down = (row+1..heightmap.len())
        .take_while(|&i| heightmap[i][col].height < self.height)
        .collect::<Vec<_>>()
        .len()
        .add(1)
        .min(heightmap.len() - row - 1);

      let view_left = (0..col).rev()
        .take_while(|&j| heightmap[row][j].height < self.height)
        .collect::<Vec<_>>()
        .len()
        .add(1)
        .min(col);

      let view_right = (col+1..heightmap[row].len())
        .take_while(|&j| heightmap[row][j].height < self.height)
        .collect::<Vec<_>>()
        .len()
        .add(1)
        .min(heightmap[row].len() - col - 1);

      view_up * view_down * view_left * view_right
    }
}

fn part1(heightmap: &mut Vec<Vec<Cell>>) -> usize {
  for row in heightmap.iter_mut() {
    let mut min_visible_height = 0;
    for Cell { height, visible } in row.iter_mut() {
      if *height >= min_visible_height {
        min_visible_height = *height + 1;
        *visible = true;
      } 
    }

    min_visible_height = 0;
    for Cell { height, visible } in row.iter_mut().rev() {
      if *height >= min_visible_height {
        min_visible_height = *height + 1;
        *visible = true;
      } 
    }
  }

  for col_ix in 0..heightmap[0].len() {
    let mut min_visible_height = 0;
    for row_ix in 0..heightmap.len() {
      let Cell { height, visible } =  &mut heightmap[row_ix][col_ix];
      
      if *height >= min_visible_height {
        min_visible_height = *height + 1;
        *visible = true;
      } 
    }

    min_visible_height = 0;
    for row_ix in (0..heightmap.len()).rev() {
      let Cell { height, visible } =  &mut heightmap[row_ix][col_ix];
      
      if *height >= min_visible_height {
        min_visible_height = *height + 1;
        *visible = true;
      } 
    }
  } 

  heightmap.iter()
    .flatten()
    .filter(|cell| cell.visible)
    .collect::<Vec<_>>()
    .len()
}
  

fn part2(heightmap: &Vec<Vec<Cell>>) -> usize {
  heightmap.iter().enumerate()
    .flat_map(|(i, row)| {
      row.iter().enumerate()
        .map(move |(j, cell)| cell.scenic_score(&i, &j, heightmap))
    }).max().unwrap()
}

fn main() {
  let input = std::fs::read_to_string("inputs/day08.txt")
    .expect("Error reading input!");

  let mut heightmap: Vec<Vec<Cell>> = input.lines()
    .map(|line| {
      line.chars()
        .map(|char| Cell { height: char.to_digit(10).unwrap(), visible: false })
        .collect()
    }).collect();

  println!("{}", part1(&mut heightmap));
  println!("{}", part2(&heightmap));
}
