use std::fs;
use std::collections::{HashSet, HashMap, hash_set::Intersection, hash_map::RandomState};

fn alphabet_encoding(c:&char) -> i32 {
    let encoding_dict:HashMap<char, i32> = HashMap::from ([
        ('a',1), ('b',2), ('c',3), ('d',4), ('e',5), ('f',6), ('g',7), ('h',8), ('i',9), ('j',10),
        ('k',11), ('l',12), ('m',13), ('n',14), ('o',15), ('p',16), ('q',17), ('r',18), ('s',19), ('t',20),
        ('u',21), ('v',22), ('w',23), ('x',24), ('y',25), ('z',26),
        ('A',27), ('B',28), ('C',29), ('D',30), ('E',31), ('F',32), ('G',33), ('H',34), ('I',35), ('J',36),
        ('K',37), ('L',38), ('M',39), ('N',40), ('O',41), ('P',42), ('Q',43), ('R',44), ('S',45), ('T',46),
        ('U',47), ('V',48), ('W',49), ('X',50), ('Y',51), ('Z',52)
    ]);

    return *encoding_dict.get(c).unwrap();
}

fn create_set_from_string(s:String) -> HashSet<char> {
    return HashSet::from_iter(s.chars());
}

fn challenge1(v:Vec<String>) {
    let mut total:i32 = 0;

    for s in v {
        let set1 = create_set_from_string(s[0..s.chars().count() / 2].to_string());
        let set2 = create_set_from_string(s[s.chars().count() / 2..s.chars().count()].to_string());
        let intersection:Intersection<char, RandomState> = set1.intersection(&set2);

        for c in intersection {
            total += alphabet_encoding(c);
        }
    }

    println!("{total:?}");

}

fn challenge2(v:Vec<String>) {
    let mut total:i32 = 0;
    let mut i:usize = 1;

    let mut l:[HashSet<char>; 3] = [HashSet::new(), HashSet::new(), HashSet::new()];

    for s in v {
        l[i % 3] = create_set_from_string(s);
        if (i % 3) == 0 {
            let it = l.iter();
            let intersection = it.next().map(|set| it.fold(set, |set1, set2| &(set1 & set2)));
            println!("{intersection:?}");

        }

        // for c in intersection {
        //     total += alphabet_encoding(c);
        // }
        i += 1;
    }

    println!("{total:?}");

}

fn main() {
    let contents: Vec<String> = fs::read_to_string(String::from("../Input/day3_input.txt"))
        .expect("Should have found file, but didn't.")
        .split('\n')
        .map(String::from)
        .collect();

    challenge1(contents);
    


   
}
