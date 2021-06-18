#[allow(dead_code)]
fn is_palindrome(n: u64) -> bool{
    let mut i = n;
    let mut rev: u64 = 0;
    while i > 0{
        let temp = i % 10;
        rev = 10 * rev + temp;
        i = i / 10;
    }
    n == rev
}

fn solve(){
    let mut best: u64 = 0;
    for i in 100..1000{
        for j in 100..1000{
            let temp = i * j;
            if is_palindrome(temp) && temp > best{
                best = temp
            }
        }
    }
    println!("{}", best)
}

fn main(){
    solve();
}
