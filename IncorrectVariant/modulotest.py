import random

totalcount = 1000

startcounter = 0

for count in range(totalcount):
    startcounter = startcounter +1
    merderler = startcounter % 20

    if merderler == 0:
        stringo = str(merderler)+" Things "+str(startcounter)
        print(stringo)
    print(startcounter)