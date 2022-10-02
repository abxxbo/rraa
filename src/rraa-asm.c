#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>

#include "asm.h"

// Memory layout of a RRAA CPU
short memory[STACK_END];
short ip = 0;


// Write bytes to a file
void write_bytes(char* file, uint8_t* bytes, int b_write){
  FILE* wr_ptr = fopen(file, "wb");
  fwrite(bytes, b_write, 1, wr_ptr);
  fclose(wr_ptr);
}


char* read_file_to_buf(char* filename){
  char* buffer = 0;
  long length;
  FILE* f = fopen (filename, "rb");

  if (f) {
    fseek (f, 0, SEEK_END);
    length = ftell (f);
    fseek (f, 0, SEEK_SET);
    buffer = malloc (length);
    if (buffer) fread(buffer, 1, length, f);
    fclose(f);
  }
  return buffer;
}

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

  char* program = read_file_to_buf(file);
  while(*program != 0){
    char c = *program;
    
    *program++;
  }
  
  return 0;
}