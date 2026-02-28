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
}

