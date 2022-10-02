#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include <stdbool.h>

#include "asm.h"

// Memory layout of a RRAA CPU
short memory[STACK_END];
short ip = 0;


int main(int argc, char** argv){
  if(argc < 2){
    fprintf(stderr,"usage: rasm  [file] [--no-krnl]");
    return 2;
  }

  char* file = argv[1];
  bool no_krnl = false; // assume false
  char* output_file = "a.out";  
  
  for(int i = 0; i < argc; i++)
    if(strcmp(argv[i], "--no-krnl") == 0) no_krnl = true;

  uint8_t buffer[1024];
  FILE* fp = fopen(file, "rb");
  fread(buffer, 1024, 1, fp);

  // File is in buffer, read.

  return 0;
}