# Interrupt Lookup Table

# `INT 0x01`

|`b0`|`b1`|`operation`|
|----|----|-----------|
|  0 |`c` | Print `c` to serial out|

# `INT 0x02`
Gets 1 character from keyboard and stores it in `b1` (as ASCII)

## `test.rraa`
```rraa
@ example:
LDA b1 <- 0x00
INT 0x02
@ print out
@ (we are assuming that b0 =/= 0)
LDA b0 <- 0x00
INT 0x01
```

## Shell
```
$ rraa-asm.py --source test.rraa --output aout
Assembled test.rraa in 0.0047s
$ rrra-emu.py --bin aout
gg
```
(assuming that `g` was inputted into the program)