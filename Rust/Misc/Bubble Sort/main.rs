use rand::Rng;


fn main() {
    let mut rng = rand::thread_rng();

    let vec_len:usize = 100000;
    let mut vec:Vec<i32> = Vec::new();
    for _ in 0..vec_len {
        let val:i32 = rng.gen();
        vec.push(val);
    }

    println!("Before Sort: {:?}", vec);

    for i in 0..vec_len {
        for j in 0..vec_len-i-1 {
            if vec[j] > vec[j+1] {
                let temp:i32 = vec[j];
                vec[j] = vec[j+1];
                vec[j+1] = temp;
            }
        }
    }

    println!("After Sort: {:?}", vec);
}
