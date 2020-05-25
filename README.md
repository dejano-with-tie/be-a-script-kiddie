Inspired by [liveoverflow](https://www.youtube.com/playlist?list=PLhixgUqwRTjxglIswKp9mpkfPNfHkzyeN) youtube channel.

## Resources
- [byte flipping](https://www.sentinelone.com/blog/breaking-and-evading/)
- [smashing the stack for fun and profit](http://phrack.org/issues/49/14.html)
- [https://exploit.education/](https://exploit.education/)

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
objdumo -t		- grap all symbols (can be used for mem inspection)
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
continue (c)        - continue
r < file			- provide input from file to run
break [address]			- set breakpoint, for example break *main, break *0x00005555555551fb
[enter]				- repeat previous command
info registers			- print registers
info break			- list breakpoints
del [break-point-num]		- remove breakpoint
set $eax=0			- set value of $eax register to 0
x/s [address]			- examin address value (string?)
x/wx $esp+0x5c          - examine value of stack-pointer+0x5c in hexadecimal format
x/24wx $esp             - examine 24 addresses starting from stack pointer (examine stack)
layout asm			- disassembled code always visible
layout regs			- regs visible
focus asm			- make assembly window active for scrolling
focus regs			- make register window active for scrolling
info proc mappings  - see memory mappings
```

#### hooks
list of commands to be executed when execution stops on break point. Example:
```
define hook-stop
> x/24wx $esp       - print stack
> x/2i $eip         - print next two instructions
> end
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

### Converting numbers (hex/bin/dec)
- convert hex to char: chr(hex)
- int('1111', 2)
- hex(...)
- "\x41\xffABCD".encode('hex')
- check struct library
	- unpack()
	- pack()
jj

---
## Assembly
- byte
	- 8 bits
- word
	- 32bit on 32bit arhitecture
	- 64bit on 64bit arhitecture


#### General purpose registars
```
eax				- first 32 bits of 64bit rax registar
```

#### Reserved registars
```
esp/rsp/sp			- stack pointer
eip/rip/ip			- instruction pointer (program counter)
ebp/rbp/bp      - base pointer register
```

#### instructions
```
lea                - load effective address
```
---
Buffer overflow notes


---
## Challenges

### Crack me

Find a key from small binary program.

- [https://crackmes.de](http://crackmes.de)
