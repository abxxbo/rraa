#pragma once

/* Memory layout */
#define BOOT_BEGIN  0x0000
#define BOOT_END    0x00ff

#define PROG_BEGIN  0x0100
#define PROG_END    0x1000

#define RAM_BEGIN   0x1001
#define RAM_END     0x2000

#define STACK_BEGIN 0x2001
#define STACK_END   0x200f


/* Opcodes */
#define LDA         0xd2    // Load address
#define JMP         0xe8    // Jump to address


/** Arithmetic **/
#define ADD         0xc0    // Add
#define SUB         0xc1    // Subtract
#define DIV         0xc2    // Divide
#define MUL         0xc3    // Multiply

#define NOP         0x44
#define HLT         0xff

/** Stack **/
#define PUSHB       0xca    // Push byte
#define POPB        0xac    // Pop byte

/** Bitwise **/
#define AND         0x72
#define OR          0x73
#define XOR         0x74

/** Interrupts **/
#define EXC         0x40
#define INT         0x39
#define STOI        0x38