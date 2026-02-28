# Nand2Tetris Project 6: Hack Assembler (Python)
# Author: James

import sys
# Pulled Translation tables from Nand2Tetris Chapter 6
DEST_TABLE = {
    None: "000",
    "M": "001",
    "D": "010",
    "MD": "011",
    "A":  "100",
    "AM": "101",
    "AD": "110",
    "AD": "110",
    "AMD": "111"
}

JUMP_TABLE = {
    None:"000",
    "JGT": "001",
    "JEQ": "010",
    "JGE": "011",
    "JLT": "100",
    "JNE": "101",
    "JLE": "110",
    "JMP": "111"
}

COMP_TABLE = {
    "0":   "0101010",
    "1":   "0111111",
    "-1":  "0111010",
    "D":   "0001100",
    "A":   "0110000",
    "!D":  "0001101",
    "!A":  "0110001",
    "-D":  "0001111",
    "-A":  "0110011",
    "D+1": "0011111",
    "A+1": "0110111",
    "D-1": "0001110",
    "A-1": "0110010",
    "D+A": "0000010",
    "D-A": "0010011",
    "A-D": "0000111",
    "D&A": "0000000",
    "D|A": "0010101",
    "M":   "1110000",
    "!M":  "1110001",
    "-M":  "1110011",
    "M+1": "1110111",
    "M-1": "1110010",
    "D+M": "1000010",
    "D-M": "1010011",
    "M-D": "1000111",
    "D&M": "1000000",
    "D|M": "1010101"
}


import sys

if len(sys.argv) != 2:
    print("Usage: python assembler.py Add.asm")
    sys.exit(1)

input_filename = sys.argv[1]
dot_at = input_filename.rfind('.')
output_filename = f"{input_filename[:dot_at]}.lines"


# Symbol table 
symbol_table = {
    "SP": 0,
    "LCL": 1,
    "ARG": 2,
    "THIS": 3,
    "THAT": 4,
    # R0 to R15
}
for i in range(16):
    symbol_table[f"R{i}"] = i

symbol_table["SCREEN"] = 16384
symbol_table["KBD"]    = 24576

rom_address = 0  # current instruction address

with open(input_filename, 'r') as file_in:
    with open(output_filename, 'w') as file_out:
        for raw_line in file_in:
            line = raw_line.strip()

           
            if not line or line.startswith('//'):
                continue

            if line.startswith('(') and line.endswith(')'):
                label = line[1:-1].strip()
                if label in symbol_table:
                    print(f"Warning: duplicate label '{label}'")
                else:
                    symbol_table[label] = rom_address
                file_out.write(f"LABEL: {label} → address {rom_address}\n")
             
                continue

           
            file_out.write(f"{rom_address:3d}: {line}\n")
            rom_address += 1





