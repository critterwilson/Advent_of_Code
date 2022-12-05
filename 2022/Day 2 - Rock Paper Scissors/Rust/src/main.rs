use std::fs; // File system
use std::collections::HashMap;

static SCORE: HashMap<char, i32> = HashMap::from([
    ('A',1),
    ('B',2),
    ('C',3),
    ('X',1),
    ('Y',2),
    ('Z',3),
]);
const WIN: [&str; 3] = ["AZ", "BX", "CY"];
const TIE: [&str; 3] = ["AX", "BY", "CZ"];

fn main() {
    let file_path = "../Input/day2_input.txt";
    println!("In file {file_path}");

    let contents = fs::read_to_string(file_path)
        .expect("Should have been able to read the file");

}