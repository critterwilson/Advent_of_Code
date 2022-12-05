use std::fs;

fn print_type_of<T>(_: &T) {
    println!("{}", std::any::type_name::<T>())
}

fn main() {
    let file_path = "../Input/day1_input.txt";
    println!("In file {file_path}");

    let contents: &str = &fs::read_to_string(file_path)
      .expect("Should have been able to read the file");
    print_type_of(&contents);

    let vectorized_contents:Vec<&str> = contents
                                          .split("\n\n")
                                          .collect();
    // print_type_of(&vectorized_contents);

    let vector_of_vectors: Vec<Vec<i32>> = vectorized_contents
                                              .iter()
                                              .map(|s| s.split("\n")
                                                .map(|s| s.to_string()
                                                  .parse::<i32>().
                                                  unwrap())
                                                .collect())
                                              .collect();
    // print_type_of(&vector_of_vectors);

    let mut vector_of_totals: Vec<i32> = vector_of_vectors
                                       .iter()
                                       .map(|v| v.iter()
                                         .sum())
                                       .collect();
    // print_type_of(&vector_of_totals);
    vector_of_totals.sort_by(|a, b| b.cmp(a));

    let highest = vector_of_totals[0];
    let top_3_highest: i32 = vector_of_totals.get(0..3)
                                 .unwrap()
                                 .iter()
                                 .sum();
    println!("Highest Calorie Value: {}", vector_of_totals[0]);
    println!("Highest Calorie Value: {}", top_3_highest);
}
