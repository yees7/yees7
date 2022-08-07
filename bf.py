from sys import argv

inpfile = argv[1]
output = None
if len(argv) == 3:
    output = argv[2]

def debug(text):
    if output:
        with open(output, 'a') as db:
            db.write(text)
    else:
        print(text, end="")

def interpret(code):
    array = [0]
    pointerLocation = 0
    i = 0
    c = 0
    while i < len(code):
        if code[i] == '<':
            if pointerLocation > 0:
                pointerLocation -= 1
        elif code[i] == '>':
            pointerLocation += 1
            if len(array) <= pointerLocation:
                array.append(0)
        elif code[i] == '+':
            array[pointerLocation] += 1
        elif code[i] == '-':
            if array[pointerLocation] > 0:
                array[pointerLocation] -= 1
        elif code[i] == '.':
            debug(chr(array[pointerLocation]))
        elif code[i] == ',':
            x = input("Input:")
            try:
                y = int(x)
            except ValueError:
                y = ord(x)
            array[pointerLocation] = y
        elif code[i] == '[':
            if array[pointerLocation] == 0:
                open_braces = 1
                while open_braces > 0:
                    i += 1
                    if code[i] == '[':
                        open_braces += 1
                    elif code[i] == ']':
                        open_braces -= 1
        elif code[i] == ']':
            open_braces = 1
            while open_braces > 0:
                i -= 1
                if code[i] == '[':
                    open_braces -= 1
                elif code[i] == ']':
                    open_braces += 1
            i -= 1
        i += 1

if output:
    open(output, 'w').close()
with open(inpfile) as inp:
    interpret(inp.read())
