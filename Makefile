CC 			:= gcc
CFLAGS	:= -Wall -std=c99 -Wextra -g

all: rraa-asm

rraa-asm: src/rraa-asm.c
	mkdir -p bin/
	$(CC) $^ $(CFLAGS) -o bin/rasm