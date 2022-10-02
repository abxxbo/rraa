#include <stdio.h>
#include <stdint.h>

/* Memory layout */
#define BOOT_BEGIN  0x0000
#define BOOT_END    0x00FF

#define PROG_BEGIN  0x0100
#define PROG_END    0x1000

#define RAM_BEGIN   0x1001
#define RAM_END     0x2000

#define STACK_BEGIN 0x2001
#define STACK_END   0x200F

// Memory layout of a RRAA CPU
short memory[STACK_END];
short ip = 0;



int main(){
  return 0;
}