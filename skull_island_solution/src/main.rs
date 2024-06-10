use std::{fs::File, io::Read};
use crypto::{aes, blockmodes, buffer::{ReadBuffer, RefReadBuffer, RefWriteBuffer, WriteBuffer}};

use image::GrayImage;
use ndarray::{s, Array2};

const SUPERSECRET: &str = "ThisIsASuperSecretAndHiddenPaswd";


fn main() {
    let mut f = File::open("lava").unwrap();
    let mut state = Array2::from_elem((512, 512), false);  

    for i in 0..512*512 {
        let mut buf = [0u8;1];
        f.read_exact(&mut buf).unwrap();
        state[(i/512, i%512)] = if buf[0] == 1 {true} else {false};
    }

    if let Some(image) = GrayImage::from_vec(512, 512, state.map(|&x| if x {255} else {0}).into_raw_vec()){
        image.save("outputs/image200.png").unwrap();
    }

    for i in (0..150).rev() {
        state = step(&state, i);
        if let Some(image) = GrayImage::from_vec(512, 512, state.map(|&x| if x {255} else {0}).into_raw_vec()){
            image.save(format!("outputs/image{}.png", i)).unwrap();
        }
    }


    let view = state.slice(s![512/2-32..512/2+32, 512/2-32..512/2+32]).to_owned();

     

    let mut bytes:Vec<u8> = vec![];

    
    for i in (0..64*64).step_by(8) {
        let mut val:u8 = 0;
        for bit in 0..8 {
            if view[((i+bit)/64, (i+bit)%64)] {
                val |=  1 << (7-bit);
            }   
        }
        bytes.push(val);
    }

    println!("{}", bytes.iter().map(|&x| format!("{:02X}", x)).collect::<Vec<String>>().join("") );


    let mut decryptor = aes::ecb_decryptor(aes::KeySize::KeySize256, SUPERSECRET.as_bytes(), blockmodes::NoPadding);


    let mut output = Vec::<u8>::new();
    let mut readbuf = RefReadBuffer::new(&bytes);
    let mut buffer = [0; 4096];
    let mut writebuf = RefWriteBuffer::new(&mut buffer);


    loop {
        let result = decryptor.decrypt(&mut readbuf, &mut writebuf, true);

        output.extend(writebuf.take_read_buffer().take_remaining().iter().map(|&x| x));

        match result {
            Ok(crypto::buffer::BufferResult::BufferOverflow) => (),
            Ok(crypto::buffer::BufferResult::BufferUnderflow) => break,
            Err(e) => panic!("{:?}", e),
        }
    }
    
println!("{}", String::from_utf8(output).unwrap());
    
}



fn step(state: &Array2<bool>, step:usize) -> Array2<bool> {
    let mut nextstate = Array2::from_elem((512, 512), false);

    let offset = (step % 3) as i32;

    let mut y = -offset;

    while y < 512 {
        let mut x = -offset;
        while x < 512 {
            let mut num_alive = 0;

            for dy in 0..3 {
                for dx in 0..3 {
                    if x + dx as i32 >= 0 && y + dy as i32 >= 0 {
                        match  state.get(((y+ dy as i32) as usize, (x + dx as i32) as usize)) {
                            Some(&is_alive) => {
                                if is_alive {num_alive += 1}
                            },
                            None => (),
                        }
                    } else {
                        
                    }
                    
                }
            }

            for dy in 0..3 {
                for dx in 0..3 {
                    if x + dx as i32 >= 0 && y + dy as i32 >= 0 {
                        match nextstate.get_mut(((y+ dy as i32) as usize, (x + dx as i32) as usize)) {
                            Some(nospot) => {
                                if num_alive == 4 || num_alive == 5 {
                                    *nospot = !state[((y+ dy as i32) as usize, (x + dx as i32) as usize)];
                                } else {
                                    *nospot = state[((y+ dy as i32) as usize, (x + dx as i32) as usize)];
                                }
                            },
                            None => (),
                        }
                    }
                }
            }

            x += 3
        }
        y += 3
    }

    nextstate

}
