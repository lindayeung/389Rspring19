# Crypto II Writeup

Name: Linda Yeung
Section: 0201

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Linda Yeung

## Assignment Writeup

### Part 1 (70 Pts)
The flag is: CMSC389R-{m3ss@g3_!n_A_b0ttl3} 



### Part 2 (30 Pts)

1. CBC is more secure because each pixel is uniformly encrypted at random. ECB on the other hand
encrypts the bits but the same bits are encrypted to the same output, so that an attacker could see the layout and outline of the original picture even though
the pixels are not exactly the same. In our example its clear that the image is a rectangle and a circle, because those pixels were the same color
so they generated the same output encrypted colors.

2. CBC is more secure because the encryption of the block is initialized with a different IV every time based on the output of the last block. This ensures
that with each subsequent block, it's not fed the same input so the same bits do not produce the same encrypted bits. The chaining of blocks gives the property of unifromly random which makes CBC more secure. 

