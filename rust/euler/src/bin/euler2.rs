#![allow(dead_code)]

fn fibonacci_at_index(n: i64) -> i64{
    match n{
        0 => 1,
        1 => 1,
        _ => fibonacci_at_index(n-1) + fibonacci_at_index(n-2),
    }
}
fn fibonacci_pat_match(bound: i64) -> i64{
    let mut idx = 0;
    let mut current = fibonacci_at_index(0);
    let mut res = 0i64;
    while current <  bound{
        res += current;
        idx += 1;
        current = fibonacci_at_index(idx);
    }
    res
}

fn naive() -> i64{
    let mut a: i64 = 0;
    let mut b: i64 = 1;
    let mut s: i64 = 0;
    while a < 4000000{
        if a % 2 == 0{
            s += a;
        }
        let temp = a + b;
        a = b;
        b = temp;
    }
    s
}
fn main(){
    println!("{}", fibonacci_pat_match(4_000_000))
}
