asm = []
gen = []

with open('/home/alfie/Projects/binary.txt', 'r') as file:
    asm = [line.strip() for line in file]


def deassemble(op, opx, opy, opz):
    if op == "00001":
        op = "mvr"
    if op == "00010":
        op = "mvm"#do smth
    if op == "00011":
        op = "mar"#do smth
    if op == "00100":
        op = "rtm"#do smth
    if op == "00101":
        op = "mtr"#do smth
    if op == "00110":
        op = "mrr"#do smth
    if op == "00111":
        op = "add"#do smth
    if op == "01000":
        op = "sub"#do smth
    if op == "01001":
        op = "mul"#do smth
    if op == "01010":
        op = "div"#do smth
    if op == "01011":
        op = "mod"#do smth
    if op =="01100":
        op = "jmp"#do smth
    if op == "01101":
        op = "jeq"#do smth
    if op == "01110":
        op = "jne"#do smth
    if op == "01111":
        op = "jez"#do smth
    if op == "10000":
        op ="jnz" #do smth
    if op == "10001":
        op ="inc" #do smth
    if op == "10010":
        op ="dec"#do smth
    if op == "10011":
        op = "drw"#do smth
    if op == "10100":
        op = "adr"#do smth
    if op == "10101":
        op ="sbr"#do smth
    if op == "10110":
        op = "jmr"#do smth
    if op == "10111":
        op = "dtr"#do smth
    if op == "11000":
        op = "rtd"#do smth
    if op == "11001":
        op = "dtm"#do smth
    if op == "00000":
        op = "nop"
    opx = int(opx, 2)
    opy = int(opy, 2)
    opz = int(opz, 2)
    return op, opx, opy, opz



for i in range(len(asm)):
    line = asm[i]

    # Extract op, opx, opy, opz
    op = line[0:5]
    opx = line[5:26]  # This should remain a string
    opy = line[26:45]  # This should remain a string
    opz = line[45:64]  # This should remain a string

    # Deassemble and capture return values
    op, opx, opy, opz = deassemble(op, opx, opy, opz)

    # Create the output string
    gen.append(f"{op} {opx} {opy} {opz}")
    print(gen[-1])  # Print the latest entry


with open("deassembledcode.txt", "w") as wr:
    wr.write("\n".join(gen))



