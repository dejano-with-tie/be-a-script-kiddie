## Tools
GDB, [hopper](http://www.hopperapp.com/), [ida](https://www.hex-rays.com/products/ida/), [radare2](https://github.com/radare/radare2)

### Commands
```
file 			- print file info
man ascii
hexdump -C
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

---
## Assembly

```
rip/eip/ip			- instruction pointer (program counter)
esp/rsp/sp			- stack pointer
eax				- first 32 bits of 64bit rax registar
```

---
## Challenges

### Crack me

Find a key from small binary program.

- [https://crackmes.de](http://crackmes.de)
