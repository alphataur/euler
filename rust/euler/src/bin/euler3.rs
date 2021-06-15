fn is_prime(n: u64) -> bool {
        (2..n).all(|divisor| n % divisor != 0)
}
fn first_factor(n: u64) -> u64{
    for i in 2..n{
        if n % i == 0{
            return i;
        }
    }
    return 1;
}
fn faster(n: u64) -> u64{
    let mut i: u64 = n;
    while i != 1{
        if is_prime(i){
            return i;
        }
        let first = first_factor(i);
        i /= first;
    }
    return 1u64;
}
fn main(){
    println!("{}", faster(600851475143))
}
