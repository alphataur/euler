#[allow(dead_code)]

fn sieve_of_erat() -> [bool; 1999999]{
    let mut sieve: [bool; 1999999] = [true; 1999999];
    let n: usize = 2000000;
    for i in 2..n{
        if !sieve[i-2]{
            continue;
        }
        for j in ((2*i)..n).step_by(i){
            sieve[j-2] = false;
        }
    }
    sieve
}

fn main(){

    let x = sieve_of_erat();
    let mut s: usize = 0;
    let n: usize = 2000000;
    for i in 2..n{
        if x[i-2]{
            s += i;
        }
    }
    println!("{}", s);
}
