fn solve() -> i64{
    let mut a: i64 = 0;
    for i in 1..1000{
        if i % 3 == 0 || i % 5 == 0{
            a += i;
        }
    }
    a
}

fn main(){
    println!("{}", solve())
}
