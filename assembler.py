import argparse
parser = argparse.ArgumentParser(description="File to be assembled")
parser.add_argument("input_value", type=str, help="File to be assembled")
args = parser.parse_args()
fl = args.input_value 

print("test")


import os
if not os.path.exists("/home/alfie/Projects/" + fl):
    print("/home/alfie/Projects/" + fl, "doesnt exist")
binarylines = [0]
asm = []
parsedtxt = []
generatedtxt = []
with open('/home/alfie/Projects/' + fl, 'r') as file:
    asm = [line.strip() for line in file]

memstart = asm[0]



def parse():
    global parsedtxt
    parsedtxt = list(filter(None, asm))
    print(parsedtxt)


def stringhandler(op, opx, opy, opz):

    if op == "mov" and opx[0] == "'" and opy[0] == "$": ###e.g mov 'hello' $1
        charcode = opx.replace("'", "").lower()
        codes = [ord(c) - 96 for c in charcode]
        binarylines[0] = f"mov {codes[0]} ${opy[1:]}"
        for k in range (len(opx.replace("'", "")) - 1):
            binarylines.append(f"mov {codes[k+1]} ${k + 1 + int(opy[1:])}")
            print("added new line of code:", f"mov {codes[k+1]} ${k + 1 + int(opy[1:])}")
        binarylines.append(f"mov 0 ${k + 1 + int(opy[1:])}")




def decode(lne, memstart, i):
    try:
        op = lne.split(" ")[0]
    except:
        op=0

    try:
        opx = lne.split(" ")[1]
    except:
        opx = 0

    try:
        opy = lne.split(" ")[2]
    except:
        opy=0

    try:
        opz = lne.split(" ")[3]
    except:
        opz = 0

    stringhandler(op, opx, opy, opz)

    if op[0] == ".":
        op = 00000
    if op == "mov":
        if opx[0] == "R":
            if opy[0] == "$":
                op = "00100"

        elif opx[0] == "$":
            if opy[0] == "R":
                op = "00101"
            if opx[1] == "R" and opy[0] == "R":
                op = "00110"
        else:
            if opy[0] == "R":
                op = "00001"
            if opy[0] == "$":
                op = "00010"
            if opy[0] == "$" and opy[1] == "R":
                op == "00011"


    if op == "mvr":
        op = "00001"
    if op == "mvm":
        op = "00010"#do smth
    if op == "mar":
        op = "00011"#do smth
    if op == "rtm":
        op = "00100"#do smth
    if op == "mtr":
        op = "00101"#do smth
    if op == "mrr":
        op = "00110"#do smth
    if op == "add":
        op = "00111"#do smth
    if op == "sub":
        op = "01000"#do smth
    if op == "mul":
        op = "01001"#do smth
    if op == "div":
        op = "01010"#do smth
    if op == "mod":
        op = "01011"#do smth
    if op =="jmp":
        op = "01100"#do smth
        if opx[0] == ".":
            opx = parsedtxt.index(opx)
            print(opx)
                
    if op == "jeq":
        op = "01101"#do smth
        if opx[0] == ".":
            opx = parsedtxt.index(opx)


    if op == "jne":
        op = "01110"#do smth
        if opx[0] == ".":
            opx = parsedtxt.index(opx)

    if op == "jez":
        op = "01111"#do smth
        if opx[0] == ".":
            opx = parsedtxt.index(opx)

    if op == "jnz":
        op ="10000" #do smth
        if opx[0] == ".":
            opx = parsedtxt.index(opx)

    if op == "inc":
        op ="10001" #do smth
    if op == "dec":
        op ="10010"#do smth
    if op == "drw":
        op = "10011"#do smth
    if op == "adr":
        op = "10100"#do smth
    if op == "sbr":
        op ="10101"#do smth
    if op == "jmr":
        op = "10110"#do smth
    if op == "dtr":
        op = "10111"#do smth
    if op == "rtd":
        op = "11000"#do smth
    if op == "dtm":
        op = "11001"#do smth
    if op == "nop":
        op = "00000"
    else:
        print("Error: Operation: ", op, " does not exist")
    print(parsedtxt[i])
    parsedtxt[i] = lne.replace(",", "").replace("$","").replace("R","")
    print("this is parsed text: ", parsedtxt[i])
    try:
        testopx = parsedtxt[i].split(" ")[1]
    except:
        testopx = "0"
    if not testopx[0] == ".":
        try:
            opx = parsedtxt[i].split(" ")[1]
        except:
            opx = 0

        try:
            opy = parsedtxt[i].split(" ")[2]
        except:
            opy=0

        try:
            opz = parsedtxt[i].split(" ")[3]
        except:
            opz = 0

    print(parsedtxt[i])
    print("new opx for verify: ", opx)

    return op, opx, opy, opz

#####START########

parse()
print("text: ", parsedtxt)

##generate binaries##
for i in rang(len(parsedtxt)):
    try:
        op = parsedtxt[i].split(" ")[0]
    except:
        op=0

    try:
        opx = parsedtxt[i].split(" ")[1]
    except:
        opx = 0

    try:
        opy = parsedtxt[i].split(" ")[2]
    except:
        opy=0

    try:
        opz = parsedtxt[i].split(" ")[3]
    except:
        opz = 0
    stringhandler(op, opx, opy, opz)

  

##for i in range(len(parsedtxt)):
#    lne = parsedtxt[i]
#     op,opx,opy,opz = decode(lne, int(memstart), i)
#    try:
#        opx = format(int(opx), "021b")
#        opy = format(int(opy), "019b")
#        opz = format(int(opz), "019b")
#    except:
#        pass
#    operation = str(op) + str(opx) + str(opy) + str(opz)
#    print(operation)
#    try:
#        generatedtxt.append(str(operation))
#    except:
#        pass


print("Final Generated Text List:")
for index, item in enumerate(generatedtxt):
    print(f"Item {index}: {item} (Type: {type(item)})")

print("ummm what/??")
for g in range(len(binarylines)):
    print(binarylines[g])


with open("binary.txt", "w") as wr:
    wr.write("\n".join(generatedtxt))

