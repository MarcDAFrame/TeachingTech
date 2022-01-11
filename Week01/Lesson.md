# Week 1: Fundamentals of computers

The following is very complex, this is not meant to fully explain all these concepts, merely give an appreciation of the layers of abstraction that tech is built upon.


## Example 1: Layers of abstraction
How computers emerge from the physical transistors

| layer # | name | description |
| --- | --- | --- |
| 1 | transistors | the physical 5-12um silicon within your CPU |
| 2 | logic gates | combination of transistors to form logic gates |
| 3 | logic circuits | combination of logic gates to form logic circuits |
| 4 | computer architecture | combination of logic circuits to form the computer architecture |
| 5 | hardware | the physical manifestation of computer architecture |
| 6 | firmware | an abstraction above hardware, so that developers don't have to write hardware specific code, reduces complexity | 
| 7 | Operating Systems | an abstraction above hardware (often built atop firmware), reduces complexity in interacting with hardware |
| 8 | Virtualization | an abstraction above Operating Systems, so that users don't have to write operating system specific software (i.e. virtual machines, docker, web browser...) |


## Example 2: Layers of abstraction for programming languages
Programming languages have been built on top of each other, sacrificing a little runtime efficiency for major increase in developer efficiency. The abstractions are to reduce complexity, and reduce the amount of work the software engineer has to do. 

| layer # | name | description |
| --- | --- | --- |
| 1 | Machine Code | lowest-level programming language, binary code that the computer can read at the hardware level |
| 2 | Assembly | low-level programming language, human readable machine code that is compiled down to machine code |
| 3 | C | mid-level programming language, abstraction above assembly | 
| 4 | python | high-level programming language, abstraction above C - python compiler is written in C |
| 5 | libraries / frameworks | provide tools and features that you don't have to program yourself |

## Example 3: Layers of abstraction for infrastructure
![iaas-paas-saas.png](<./res/iaas-paas-saas.png>)
| layer # | name | description |
| --- | --- | --- |
| 1 | on-prem / self hosting | managing your own hardware |
| 2 | Infrastructure as a Service (IaaS) | cloud providers, manage the hardware for you, you manage the software, databases... on the infrastructure |
| 3 | Platform as a Service (PaaS) | platform manages software, databases... for you, you build your app on top of these platforms |
| 4 | Software as a Service (SaaS) | software solutions made for you, require no development on your part (No Code, Google Docs, Slack...) |

## Outline
- History
- Binary
    - transistors
- Logic
    - logic gates
    - logic circuits
    - ALU
- Computer Architecture
    - Instruction Sets
        - ARM: RISC
        - x86
- Hardware
- Firmware
- Operating Systems


# History
| Gen # | Years | Description |
| --- | --- | --- |
| 1 | 1946-1959 | Vacuum tube based. |
| 2 | 1959-1965 | Transistor based. |
| 3 | 1965-1971 | Integrated Circuit based. |
| 4 | 1971-1980 | VLSI microprocessor based. |
| 5 | 1980-onwards | ULSI microprocessor based. |



# Binary
![Decimal to binary table](<./res/binary.png>)
- comprised of ones and zeros
- number of digits = number of bits
    - 8bit means 8 digits
        - 10101010
    - modern systems are typically 32bit or 64bit
    - this is where the term 8bit comes from for video games as the old video game systems (NES, Atari...) were 8bit systems
- binary is simply one of the infinite `number systems`
    - `base 10` is decimal
    - `base 16` is hexadecimal
    - `base 3` is the ternary number system
- video: https://www.youtube.com/watch?v=zDNaUi2cjv4
- calculator: https://www.rapidtables.com/convert/number/binary-to-decimal.html

## Transistors
![transistor](<./res/macro-transistor.png>)
![vacuum tube](<./res/vacuum-tubes.jpg>)
![micro transistors](<./res/micro-transistor.jpg>)

- transistors have three wires
    - **b**: Base - gate controller
    - **c**: Collector - electric supply 
    - **e**: Emitter - output

If the base is on, then the power supply through the collector is passed through to the emitter.

![binary-transistors.png](<./res/binary-transistors.png>)

Transistors enable us to represent binary with electrical systems.

These transistors can be combined to form logic


# Logic
Logic is built upon the binary system in the form of `boolean logic`

## Boolean Logic
![boolean-algebra-truth-tables.png](<./res/boolean-algebra-truth-tables.png>)


## Logic Gates
![logic gates](<./res/logic-gates.jpeg>)
- column 1: logic gate name
- column 2: logic gate symbols
- column 3: truth tables
- column 4: logic symbols

![minecraft](<./res/minecraft-logic-gates.jpg>)
- minecraft redstone is a form of logic gates

[more about the Minecraft logic gates](https://minecraft.wonderhowto.com/news/redstone-logic-gates-mastering-fundamental-building-blocks-for-creating-game-machines-0135063/)


## Logic Circuits
![logic-circuit](<./res/logic-circuit.png>)

logic circuits are combinations of multiple logic gates

### Logic Circuit: Arithmetic Logic Unit (ALU)
a component of a CPU, an ALU is a combinational digital circuit performs arithmetic and bitwise operations on integer binary numbers.

![ALU Overview](<./res/alu-overview.gif>)
![ALU Complex](<./res/alu-complex.png>)
This is a 4 bit ALU, modern computers have 32/64/80 bit ALUs. The complexity of these digital circuits grows exponentially and as such, a complete diagram of a 32+ bit ALU would not be human readable.

This is one example of a logic circuit

### Logic Circuit: Flip-Flop
a digital circuit that is used for storing 1 bit of digital data.

![flip-flop.jpg](<./res/flip-flop.jpg>)

Note, in the above diagram how the circuit feeds back into itself. This is what enables the circuit to have a concept of "memory"

### Logic Circuit: Registers 
A component of a CPU, RAM and other computer hardware, a register is a digital circuit that is used for storing **n** bits of digital data. It is comprised of a chain of **n** `flip-flops`.

These are quite complex, we will not talk about their implementation.


### Logic Circuit: Control Unit (CU)
![control-unit.gif](<./res/control-unit.gif>)

A component of a CPU, a CU directs the operations and processes of a computer. It converts coded instructions into timing and control signals that direct the operation of the other units (memory, arithmetic logic unit and input and output devices, etc.).

It sets the "clock" of a computer, during clock cycles, program data will be loaded from the primary memory (RAM) where the CU will signal different units (memory, ALU, I/O) depending on the "instruction" read from memory. In the next clock cycle the next block of data will be read and the next instruction executed.

# Computer Architecture
![computer-arch.gif](<./res/computer-arch.gif>)

computer architecture is the accumulation of all (and many more) parts from above.

The parts are orchestrated by the Control Unit and communicate over a Bus.

## Bus
is a Data highway, a communication system that transfers data between components inside a computer.

## [Computer Architecture: Further Readings](https://www.doc.ic.ac.uk/~eedwards/compsys/)

## Instruction Sets
an instruction set is the definition of operations that a control unit can perform.

### Examples of instructions

| instruction | desc |
| --- | --- |
| LOAD | load data into register |
| STORE | store data to memory |
| ADD | add data of register A and B |
| SUB | subtract data of register A and B |
| SHIFT | shift data of register A (used for multiplication / division) |
| JUMP | jump to a point in memory to begin executing from that point, used for loops (while, for...) | 
| JZ | jump if zero, used for conditional logic |

### Assembly Language
Assembly is a low-level programming language that is closely defined by the instruction set.

Assembly would look very similar to the instruction set above, but is compiled to a specific computer architecture by an `assembler` into Machine Code.

Therefore, assembly can be used to write code that will work on different computer architectures by using different `assemblers`


```
; ----------------------------------------------------------------------------------------
; Writes "Hello, World" to the console using only system calls. Runs on 64-bit Linux only.
; To assemble and run:
;
;     nasm -felf64 hello.asm && ld hello.o && ./a.out
; ----------------------------------------------------------------------------------------

          global    _start

          section   .text
_start:   mov       rax, 1                  ; system call for write
          mov       rdi, 1                  ; file handle 1 is stdout
          mov       rsi, message            ; address of string to output
          mov       rdx, 13                 ; number of bytes
          syscall                           ; invoke operating system to do the write
          mov       rax, 60                 ; system call for exit
          xor       rdi, rdi                ; exit code 0
          syscall                           ; invoke operating system to exit

          section   .data
message:  db        "Hello, World", 10      ; note the newline at the end
```


### Machine Code
machine code is the compiled version of instruction sets

An example of the compiled machine code and the instruction could be

| instruction | compiled value |
| --- | --- |
| LOAD | 0000 |
| STORE | 0001 |
| ... | ... |

```
b8    21 0a 00 00   #moving "!\n" into eax
a3    0c 10 00 06   #moving eax into first memory location
b8    6f 72 6c 64   #moving "orld" into eax
a3    08 10 00 06   #moving eax into next memory location
b8    6f 2c 20 57   #moving "o, W" into eax
a3    04 10 00 06   #moving eax into next memory location
b8    48 65 6c 6c   #moving "Hell" into eax
a3    00 10 00 06   #moving eax into next memory location
b9    00 10 00 06   #moving pointer to start of memory location into ecx
ba    10 00 00 00   #moving string size into edx
bb    01 00 00 00   #moving "stdout" number to ebx
b8    04 00 00 00   #moving "print out" syscall number to eax
cd    80            #calling the linux kernel to execute our print to stdout
b8    01 00 00 00   #moving "sys_exit" call number to eax
cd    80            #executing it via linux sys_call

* VALUES IN HEXADECIMAL *
```


### RISC and x86
both are types of instruction sets.

RISC is more modern, it's an acronym for **Reduced Instruction Set Computer**. This instruction set is run on Advanced RISC Machines (ARM) architectures which are common place on, smart phones, tablets, raspberry pis and Apple's new M1 chip. RISC instruction sets, due to it's simplicity is known for reduced energy use and better parallelization (i.e. multi-core threading).  

x86 is the more common instruction set. It is known for a complex and lengthy instruction set list. x86 was created by Intel and is the instruction set that both Intel and AMD use. Due to x86's complex instructions, it does not parallelize as well as RISC. This is a major issue with modern CPUs as individual cores are not getting faster, rather CPUs are increasing the number of cores they have.


# Hardware
Hardware is the accumulation of all (and more) of the concepts above.

All (and more) of the following components together form a modern computer. 

## RAM
Random access memory is essentially a set of transistors, logic gates and logic circuits that utilize registers to store and load data.

These logic gates need a constant supply of energy, otherwise they lose their state. This is known as volatile memory as it does not persist when the computer turns off / loses power.

## Secondary Storage
Secondary storage is persistent but typically slower than RAM.

## CPU
Computer Processing Unit, the brain of the computer is comprised of a control unit, ALUs, and registers.

GPU is essentially the same thing as the CPU, except the logic circuits it's made of are better suited for linear algebra equations. Linear algebra being the primary math behind rendering 3D model


## I/O devices
keyboards, mouse, webcams, monitors... are connected to an I/O bus where the CPU will either regularly poll for data or be 'interrupted' by the device to move input.

Most I/O devices are through universal serial bus, better known as USB.

# Firmware
Firmware is software that is written at a very low level in order to abstract complexity of working with different hardware.

An example of firmware is the BIOS which abstracts the hardware specific interfaces into one API that will work with an operating system. i.e. Windows and Linux don't need to be rewritten/recompiled for every computer, or every combination of hardware.

# Operating Systems
![os.png](<./res/os.png>)
Operating systems abstract complexity by managing computer hardware, software resources, execution of multiple processes, and provides common services for computer programs.

Operating systems abstract complexity from the developer by offering standardized APIs for interacting with hardware. The developer never has to write code specific to hardware.

## File System
an example of a standardized API is the file system. Instead of having to worry about how bits and bytes are written to an HDD the operating system manages the hardware level interactions, and presents a standardized API for developers to use to manage directories and files.

## Other abstractions that an OS provides
- process execution 
- hardware threading
- I/O device access
- memory management

