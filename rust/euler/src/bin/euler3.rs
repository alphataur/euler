fn factors(num: i64) -> Vec<i64>{
    let mut res = vec![];
    for i in 2..num{
        if num % i == 0{
            res.push(i);
        }
    }
    res
}

fn is_prime(num: i64) -> bool{
    for i in 2..num{
        if num % i == 0{
            return true
        }
    }
    return false
}

fn solve(num: i64) -> Vec<i64>{
    factors(num).into_iter().filter(|&e| is_prime(e)).collect::<Vec<_>>()
}
fn main(){
    let temp = solve(600851475143);
    println!("{}", temp.last().unwrap())
}
