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
x/s [address]			- examin address value (string?)
layout asm			- disassembled code always visible
layout regs			- regs visible
focus asm			- make assembly window active for scrolling
focus regs			- make register window active for scrolling
```


### Radare2
```
?               - help, every letter means something. Help can be triggered with letter?, for ex a?
aaa             - automaticaly analyse and autoname functions
afl             - list all functions that radare found
s               - seek. To seek to a main fn - s sys.main
pdf             - prind disassembly of current function
VV              - visual mode
                    - move with arrow keys
                    - cycle through blocks with tab
                    - ? help
                    - p cycle through different representations
r2 -d           - start radare in debug mode
db [address]    - set break point
:               - enter command mode
dc             	- continue execution
s               - step into *only in visual mode
S               - step over *only in visual mode
f7		- step into
f8		- step over
ds		- step into *only in normal
dso		- step over *only in normal
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
