#폴리오미노

x = input() #X와 . 입력
y = ""
chk = 0

while(True):
    if len(x) == 0:
        break
    if len(x) == 1:
        chk = -1
        print(chk)
        break
    if x[0] == ".":
        while(x[0] == "."):
            x = x[1:]
            y = y + "."
    if x[0:2] == "XX":
        if x[0:4] == "XXXX":
            x = x[4:]
            y = y + "A" * 4
        elif x[0:7] == "XXXXXX":
            x = x[7:]
            y = y + "A" * 4 + "B" * 2
        else:
            x = x[2:]
            y = y + "B" * 2
    else:
        chk = -1
        print(chk)
        break
if chk == 0:
    print(y)         
    


