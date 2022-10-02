#include <stdio.h>
#include <stdint.h>

#include "asm.h"

// Memory layout of a RRAA CPU
short memory[STACK_END];
short ip = 0;


// Read program into memory to assemble
uint8_t* read_program(char* file){
  uint8_t* buffer = 0;
  FILE* fp = fopen(file, "rb");
  fread(buffer, 1024, 1, fp);
  return buffer;
}

int main(){
  return 0;
}