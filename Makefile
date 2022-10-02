CC := gcc
CFLAGS := -Wall -Wextra -lraylib -lm -std=gnu99

all: rraa

rraa:
	mkdir -p bin/
	$(CC) src/remu.c $(CFLAGS) -o bin/remu

clean:
	rm a.out -rf bin