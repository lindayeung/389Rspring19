/*
 * Name: Linda
 * Section: 0201
 *
 * I pledge on my honor that I have not given or received any unauthorized
 * assistance on this assignment or examination.
 *
 * Digital acknowledgement: Linda Yeung
 */

#include <stdio.h>
#include <stdlib.h>

int main() {
  int a, b;
  a = 0xfeedface;
  b = 0x1ceb00da;

  printf("%d\n", a);
  printf("%d\n", b);

  a ^= b;
  b ^= a;
  a ^= b;

  printf("%d\n", a);
  printf("%d\n", b);
}

/* PART 2
The program takes two integer variables and assigns values to them, then prints them.
It then swaps the two variables and prints out the new swapped values!
*/
