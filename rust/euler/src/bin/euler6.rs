#[allow(dead_code)]
fn square_sum(end: u64) -> u64{
    let base = (end * (end + 1)) / 2;
    base * base
}
fn sum_square(end: u64) -> u64{
    let mut res: u64 = 0;
    for i in 1..=end{
        res += i * i;
    }
    res
}

fn solve() -> u64{
    square_sum(100) - sum_square(100)
}

fn main(){
    println!("{}", solve())
}
