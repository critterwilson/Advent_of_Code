use std::fs; // File system
use std::collections::HashMap;

fn challenge1(v: &Vec<&str>) {
    let score: HashMap<char, i32> = HashMap::from([
            ('A',1),
            ('B',2),
            ('C',3),
            ('X',1),
            ('Y',2),
            ('Z',3),
        ]);
    let win: [&str; 3] = ["A Z", "B X", "C Y"];
    let tie: [&str; 3] = ["A X", "B Y", "C Z"];

    let mut left_score: i32 = 0;
    let mut right_score: i32 = 0;

    for line in v {
        let left_move: &char = &line.chars().nth(0).unwrap();
        let right_move: &char = &line.chars().nth(2).unwrap();
        left_score += score.get(left_move).unwrap();
        right_score += score.get(right_move).unwrap();

        if win.contains(&line) {
            left_score += 6;
        }
        else if tie.contains(&line) {
            left_score += 3;
            right_score += 3;
        }
        else {
            right_score += 6;
        }
    }

    println!("My Score: {right_score}");
}

fn challenge2(v: &Vec<&str>) {
    let score: HashMap<char, i32> = HashMap::from([
            ('A',1),
            ('B',2),
            ('C',3),
            ('X',1),
            ('Y',2),
            ('Z',3),
        ]);
    let win: [&str; 3] = ["A Z", "B X", "C Y"];
    let tie: [&str; 3] = ["A X", "B Y", "C Z"];
    let moves: HashMap<char, HashMap<char, &str>> = HashMap::from([
        ('X', HashMap::from([('A',"A Z"), ('B',"B X"), ('C',"C Y")])),
        ('Y', HashMap::from([('A',"A X"), ('B',"B Y"), ('C',"C Z")])),
        ('Z', HashMap::from([('A',"A Y"), ('B',"B Z"), ('C',"C X")])),
    ]);

    let mut left_score: i32 = 0;
    let mut right_score: i32 = 0;

    for line in v {
        let actual_matchup = moves.get(&line.chars().nth(2).unwrap()).unwrap().get(&line.chars().nth(0).unwrap()).unwrap();
        println!("{line} {actual_matchup}");
        let left_move: &char = &actual_matchup.chars().nth(0).unwrap();
        let right_move: &char = &actual_matchup.chars().nth(2).unwrap();
        left_score += score.get(left_move).unwrap();
        right_score += score.get(right_move).unwrap(); 

        if win.contains(&actual_matchup) {
            left_score += 6;
        }
        else if tie.contains(&actual_matchup) {
            left_score += 3;
            right_score += 3;
        }
        else {
            right_score += 6;
        }
    }
    println!("My Score: {right_score}");
}

fn main() {
    let file_path: &str = "../Input/day2_input.txt";
    let contents: &str = &fs::read_to_string(file_path)
        .expect("Should have been able to read the file");
   
    let vectorized_contents:&Vec<&str> = &contents
        .split("\n")
        .collect();
    
    challenge1(vectorized_contents);
    challenge2(vectorized_contents);

}