"""CPU functionality."""

import sys


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256  # Ram with size of 256 bytes
        self.reg = [0] * 8
        # Below are Internal Registers
        self.pc = 0  # Program Counter
        self.ir = "00000000"
        self.mar = "00000000"
        self.mdr = "00000000"
        self.fl = "00000000"
        # Added instructions set for printing purposes
        self.instruction = {"LDI": 0b10000010,
                            "PRN": 0b01000111, "HLT": 0b00000001}

# Functions for RAM read/write
    def ram_read(self, address):
        return self.ram[address]

    def ram_write(self, address, value)
    return self.ram[address] = value

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010,  # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111,  # PRN R0
            0b00000000,
            0b00000001,  # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        # elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            # self.fl,
            # self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        # Perform REPL style execution

        while True:
            # Start the CPU. start storing instructions in IR
            self.ir = self.ram_read(self.pc)
            # Exit the program when Instruction HLT is read
            if self.ir = self.instruction["HLT"]:
                break
            # Execute other instructions
            elif self.ir = self.instruction["LDI"]:
                pass
            elif self.ir = self.instruction["PRN"]:
                pass
