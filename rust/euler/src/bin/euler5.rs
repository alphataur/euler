//fn solve(){
//println!("{:?}", (0..10)
//    // `&mut acc` in the parameter position extracts `acc` out of a mutable ref,
//    // it is NOT a definition of a mutable ref
//    .scan( 0, |acc, x| {
//        *acc = *acc + x; // also, you need to dereference `acc` to modify that
//        Some( *acc )
//    })
//    .find( |&x| x > 10 ) );
//}

type Binop = fn(u64, u64) -> u64;

fn gcd(a: u64, b: u64) -> u64{
    if b == 0{
        a
    }
    else{
        gcd(b, a % b)
    }
}

fn lcm(a: u64, b: u64) -> u64{
    (a * b) / gcd(a, b)
}


fn reductions(start: u64, end: u64) -> u64{
    let mut acc: u64 = 1;
    for i in start..end{
        acc = lcm(i, acc);
    }
    acc
}


fn main(){
    //println!("{}", lcm(1920, 1080))
    println!("{}", reductions(1, 10));
}
