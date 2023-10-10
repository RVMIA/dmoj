use std::io;

fn main() {
    let mut input = String::new();
    println!("Enter some input");
    io::stdin().read_line(&mut input).expect("failed");
    println!("{}", input);
}
