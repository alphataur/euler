#[allow(dead_code)]
fn solve() -> i64{
    let mut a: i64 = 0;
    for i in 1..1000{
        if i % 3 == 0 || i % 5 == 0{
            a += i;
        }
    }
    a
}

fn range_solve() -> i64{
    (1..1000).filter(|e| e % 3 == 0 || e % 5 == 0).sum()
}

fn main(){
    println!("{}", range_solve())
}
