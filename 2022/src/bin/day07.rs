use std::{collections::HashMap, cell::RefCell, rc::Rc};
struct Directory {
  parent: Option<Rc<RefCell<Directory>>>,
  children: HashMap<String, Rc<RefCell<Directory>>>,
  size: u32
}

impl Directory {
  fn new() -> Rc<RefCell<Directory>> {
    Rc::new(RefCell::new(
      Directory {
        parent: None,
        children: HashMap::new(),
        size: 0
      }
    ))
  }

  fn new_child(parent: &Rc<RefCell<Directory>>, name: &str) -> Rc<RefCell<Directory>> {
    let child = Rc::new(RefCell::new(
      Directory {
        parent: Some(Rc::clone(parent)),
        children: HashMap::new(),
        size: 0
      }
    ));

    let ret = Rc::clone(&child);

    parent.borrow_mut().children.insert(String::from(name), child);
    ret
  }

  fn sizes(&self, name: &String) -> Vec<(String, u32)> {
    let (parent_size, mut children_sizes): ((String, u32), Vec<(String, u32)>) = self.children.iter()
      .fold(((name.to_string(), self.size), vec![]), |((parent_name, parent_size_acc), mut children_sizes_acc), (name, subdirectory)| {
        children_sizes_acc.extend(subdirectory.borrow().sizes(name));

        ((parent_name, parent_size_acc + children_sizes_acc.last().unwrap().1), children_sizes_acc)
      });

    children_sizes.push(parent_size);
    children_sizes
  }
}

fn part1(fs: &Directory) -> u32 {
  fs.sizes(&"/".to_string())
    .into_iter()
    .filter_map(|(_name, size)| if size <= 100000 { Some(size) } else { None })
    .sum()
}
  

fn part2(fs: &Directory) -> u32 {
  let sizes = fs.sizes(&"/".to_string());
  let needed_space: u32 = 30000000 - (70000000 - sizes.last().unwrap().1);

  sizes.into_iter()
    .filter(|(_name, size)| *size >= needed_space)
    .min_by_key(|size| size.1)
    .unwrap().1
}

fn main() {
  let input = std::fs::read_to_string("inputs/day07.txt")
    .expect("Error reading input!");

  let root = Directory::new();

  input.lines()
    .skip(1)
    .filter(|line| *line != "$ ls")
    .map(|line| line.split_whitespace().collect())
    .fold(Rc::clone(&root), |directory, arguments: Vec<&str>| {
      match arguments.as_slice() {
        ["$", "cd", ".."] => Rc::clone(directory.borrow().parent.as_ref().unwrap()),
        ["$", "cd", name] => Rc::clone(directory.borrow().children.get(&String::from(*name)).unwrap()),
        ["dir", name] => {
          Directory::new_child(&directory, name);
          directory
        },
        [size, _] => {
          directory.borrow_mut().size += (*size).parse::<u32>().unwrap();
          directory
        },
        _ => directory
      }
    });

  println!("{}", part1(&root.borrow()));
  println!("{}", part2(&root.borrow()));
}
