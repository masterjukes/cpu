##  1091776 ram, 1048576 - 1221376 - screen memory
##  240*180 screen
##  8388608 memory slots in drive
##  35 reg slots
from math import floor
import turtle as t
import pygame
pygame.init()
screen_width, screen_height = 1920, 1920  # Scale up from 240x180
screen = pygame.display.set_mode((screen_width, screen_height), pygame.HWSURFACE | pygame.DOUBLEBUF)

#setup mem and stuff !!#
reg = [0] * 36
reg[35] = "rom"
ram = [0] * 1278976
dsk = [0] * 8388608
rom = []
with open('/home/alfie/Projects/binary.txt', 'r') as file:
    rom = [line.strip() for line in file]


#functions area#
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
running = True
screen.fill(BLACK)

##Draw Function##
rects_to_update = []
def drawscreen():
    screen.fill(BLACK)
    for y in range(480):
        for x in range(480):
            if ram[1048576+ y * 480 + x] != 0:
                addr = 1048576 + y * 480 + x
                print(f"Drawing at {x}, {y} (Address: {addr})")
                rect = pygame.Rect(x * 4, y * 4, 4, 4)
                pygame.draw.rect(screen, WHITE, rect)
                rects_to_update.append(rect)
    pygame.display.update(rects_to_update)
drawscreen()

#Exectute Function#
def execute(op, opx, opy, opz):
    if op == "0b00001":  #mvr
        reg[opy] = opx
    elif op == "0b00010":   #mvm
        ram[opy] = opx
    elif op == "0b00011":   #mar
        ram[reg[opy]] = opx
    elif op == "0b00100":   #rtm
        ram[opy] = reg[opx]
    elif op == "0b00101":   #mtr
        reg[opy] = ram[opx]
    elif op == "0b00110":   #mrr
        reg[opy] = ram[reg[opx]]
    elif op == "0b00111":   #add
        reg[opz] = opx + opy
    elif op == "0b01000":   #sub
        reg[opz] = opx - opy
    elif op == "0b01001":   #mul
        reg[opy] = opx * opy
    elif op == "0b01010":   #div
        reg[opy] = floordiv(opx, opy)
    elif op == "0b01011":   #mod
        reg[opy] = opx % opy
    elif op == "0b01100":   #jmp
        reg[34] = opx
    elif op == "0b01101":   #jeq
        if reg[opy] == opz:
            reg[34] = opx
    elif op == "0b01110":   #jne
        if reg[opy] != opz:
            reg[34] = opx
    elif op == "0b01111":   #jez
        if reg[opy] == 0:
            reg[34] = opx
    elif op == "0b10000":   #jnz
        if reg[opy] != 0:
            reg[34] = opx
    elif op == "0b10001":   #inc
        reg[opx] += 1
    elif op == "0b10010":   #dec
        reg[opx] = reg[opx] - 1
    elif op == "0b10011":   #drw
        drawscreen()
    elif op == "0b10100":   #adr
        reg[opz] = reg[opx] + opy
    elif op == "0b10101":   #sbr
        reg[opz] = reg[opx] - opy
    elif op == "0b10110":   #jmr
        reg[34] = reg[opx]
    elif op == "0b10111":   #dtr
        ram[opy] = dsk[opx]
    elif op == "0b11000":   #rtd
        dsk[opy] = ram[opx]
    elif op == "0b11001":   #dtm
        ram[reg[opy]] = dsk[reg[opx]]

while True:
    lists = {
    'rom': rom,
    'ram': ram
}
    mem = reg[35]
    itm = reg[34]
    operation = lists[mem][itm]
    try:
        _op = ("0b" + str(operation[0:5]))
    except (ValueError, IndexError):
        _op = 0

    try:
       _opx = int(operation[5:26], 2)
    except (ValueError, IndexError):
        _opx = 0

    try:
        _opy = int(operation[26:45], 2)
    except (ValueError, IndexError):
        _opy = 0

    try:
        _opz = int(operation[45:64], 2)
    except (ValueError, IndexError):
        _opz = 0
    reg[34] += 1
    try:
        execute(_op, int(_opx), int(_opy), int(_opz))
        #print(_op, _opx, _opy, _opz)
    except (ValueError, IndexError) as e:
        pass #print(f"Error executing instruction: {_op}, {_opx}, {_opy}, {_opz} -> {e}")
    if reg[34] == 1048576:
        reg[34] = 0

