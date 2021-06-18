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
fn solve(){
    let res = (0..=10).scan(0, | a, e|{
        *a = *a + e;
        Some(*a)
    });
    println!("{:?}", res.max());
}
fn main(){
    solve();
}
