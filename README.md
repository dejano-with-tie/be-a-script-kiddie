Inspired by [liveoverflow](https://www.youtube.com/playlist?list=PLhixgUqwRTjxglIswKp9mpkfPNfHkzyeN) youtube channel.

## Tools
GDB, [hopper](http://www.hopperapp.com/), [ida](https://www.hex-rays.com/products/ida/), [radare2](https://github.com/radare/radare2), [binary ninja](https://binary.ninja/)

### Commands
```
file 			- print file info
man ascii
hexdump -C
xxd             - hex dump or inverse
strings 		- printable characters in file
objdump -d 	 	- disassemble
objdump -x 		- headers. Interesting sections: .text, .rodata (read only section)
strace 			- trace system calls and signals (man syscalls)
ltrace 			- trace library functions (strcmp, printf..)
```


### GDB
```
set disassembly-flavor intel	- more readable syntax
disassemble main		- disassemble main fn
ni 				- next instruction (step over)
si				- step into
run (r)				- run debug
break [address]			- set breakpoint, for example break *main, break *0x00005555555551fb
[enter]				- repeat previous command
info registers			- print registers
info break			- list breakpoints
del [break-point-num]		- remove breakpoint
set $eax=0			- set value of $eax register to 0
x/s [address]			- print address value (string?)
```


### Radare2
```
?               - help, every letter means something. Help can be triggered with letter?, for ex a?
aaa             - automaticaly analyse and autoname functions
afl             - list all functions that radare found
s               - seek. To seek to a main fn - s sys.main
pdf             - prind disassembly of current function
vv              - visual mode
                    - move with arrow keys
                    - cycle through blocks with tab
                    - ? help
                    - p cycle through different representations
r2 -d           - start radare in debug mode
db [address]    - set break point
:               - enter command mode
:dc             - run a program
s               - step into
S               - step over
ood [args]      - reopen in debug mode (with args)
oodf [file]     - reopen in debug mode using the given file
dr              - show 'gpr' registers
dr <reg>=<val>  - set register value
afvn [new_name] ([old_name])  - rename argument/local
```
---
## Python

### Hex
- convert hex to char: chr(hex)

---
## Assembly
```
rip/eip/ip			- instruction pointer (program counter)
esp/rsp/sp			- stack pointer
eax				- first 32 bits of 64bit rax registar
ebp/ebp/bp      - base pointer register
```

---
## Challenges

### Crack me

Find a key from small binary program.

- [https://crackmes.de](http://crackmes.de)
