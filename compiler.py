code = input("give code:  ")
state = 0
iv = ""
iftype = 0
lin=0
le=""
l=0
v="0"
ifv = ""

#? - Print
#?§ - Newline
#?$ - Print V as Ascii
#i - Input
#f - If
#s - Input value
#v - Variable
#v= - Variable set
#v+ - Variable add 1
#v- - Variable remove 1
#A - Start loop
#g - Loop
#; - Pass

#Truth machine: ifs=0:?0;fs=1:A?1?§g;
#Hello World:   ?H?e?l?l?o?,? ?W?o?r?l?d?!?§

while lin < len(code):
    lin+=1
    le=code[lin-1:lin]
    if state == 0:
        if le == "i":
            iv = input("")
        elif le == "f":
            state = 1
        elif le == "?":
            state = 5
        elif le == "A":
            l=lin
        elif le == "g":
            lin=l-1
            le=code[lin-1:lin]
        elif le == "v":
            state = 6
        elif le == ";":
            pass
    else:
        if state == 1:
            if le=="s":
                iftype = "s"
                state = 2
            if le=="v":
                iftype = "v"
                state = 2
        elif state == 2:
            ifv = ""
            if le=="=":
                state = 3
        elif state == 3:
            if le == ":":
                if iftype == "s":
                    if iv == ifv:
                        state = 0
                    else:
                        state = 4
                if iftype == "v":
                    if v == ifv:
                        state = 0
                    else:
                        state = 4
            else:
                ifv = ifv + le
        elif state == 4:
            if le == ";":
                state = 0
        elif state == 5:
            if le == "§":
                print()
            elif le == "$":
                print(ascii(int(v)))
            else:
                print(le, end="")
            state = 0
        elif state == 6:
            state = 0
            if le == "=":
                state = 7
                ifv = ""
            elif le == "+":
                v = str(int(v)+1)
            elif le == "-":
                v = str(int(v)-1)
        elif state == 7:
            if le == ";":
                state = 0
                v = ifv
            else:
                ifv = ifv + le
print()
print()