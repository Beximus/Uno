import random
import csv
import numpy as np
rules = ['it is the same color as the tabled card','it is the same type as the tabled card', 'Wild cards can be played on any colour','If there are no allowed moves you must pick up','it is the same color and type as the tabled card','Any card can be played on a Wild Normal','You have to pick up 4 cards when a Wild Draw 4 is played','You must pick up 2 cards when a Draw 2 is played','this is an illegal move']
colorarray =['Red','Green','Blue','Yellow']

numberrun = 100000
numberillegal =2

# GENERATES DECK OF CARDS
def generateCards():
    deck =[]
    i = 0
    for i in range(4):
        wild = ['Wild','Normal']
        deck.append(wild)
        wild4 = ['Wild','Draw 4']
        deck.append(wild4)
        skips = [colorarray[i],'Skip']
        deck.append(skips)
        deck.append(skips)
        reverse = [colorarray[i],'Reverse']
        deck.append(reverse)
        deck.append(reverse)
        drawtwo = [colorarray[i],'Draw 2']
        deck.append(drawtwo)
        deck.append(drawtwo)
        zeros = [colorarray[i],"0"]
        deck.append(zeros)
        j=1
        for j in range(9):
            number = str(j+1)
            numbercard = [colorarray[i],number]
            deck.append(numbercard)
            deck.append(numbercard)
    return deck

# SELECTS CARDS
def selectCards():
    deck = generateCards()
    hand = random.choices(deck,k=7)
    table = random.choices(deck,k=1)
    return hand, table, deck    

# TRANSLATES 2D ARRAY THINGS
def translator(array):
    string = str(array[0])+" "+str(array[1])
    return string

# HAND TRANSLATOR
def handTranslator(array):
    string = ''
    for iteration, item in enumerate(array):
        string = string + translator(item)
        if iteration <len(array)-1:
            string = string+", "
        else :
            string = string+" "
    return string

# FINDS POSSIBLE MOVES AND GENERATES ARRAY OF OPTIONS FOR CSV
def playmaker():
    setup = selectCards()
    hand = setup[0]
    table = setup[1]
    table = table[0]
    deck = setup[2]
    
    playoptions =[]
    playrules =[]

    outputRow =[]
    output =[]

    randomnumber = random.randint(0,6)

    outputRow.append(translator(table)+" ")
    outputRow.append(" "+handTranslator(hand))

    # MOVE FINDER IF TREE
    if table[0] == 'Wild' and table[1] == 'Normal':
        for cards in hand:
            playoptions.append(cards)
            playrules.append(rules[5])
    elif table[0] == 'Wild' and table[1] == 'Draw 4':
        option = ['Pick up','4 cards']
        playoptions.append(option)
        playrules.append(rules[6])
    elif table[1] == 'Draw 2':
        option = ['Pick up','2 cards']
        playoptions.append(option)
        playrules.append(rules[7])
    else:
        for card in hand:
            if card[0] == table[0]:
                playoptions.append(card)
                playrules.append(rules[0])
            elif card[1]==table[1]:
                playoptions.append(card)
                playrules.append(rules[1])
            elif card[0]=='Wild':
                playoptions.append(card)
                playrules.append(rules[2])
    
    # GENERATES LIST OF POSSIBLE MOVES
    if len(playoptions)>0:
        if len(playoptions)==1:
            informationString = "You can play "+translator(playoptions[0])+" because "+str(playrules[0])
            outputRow.append(translator(playoptions[0]))
            outputRow.append(str(playrules[0]))
            output.append(outputRow)
        else:
            for iteration, item in enumerate(playoptions):
                row =[]
                row = row+ outputRow
                row.append(translator(item))
                row.append(str(playrules[iteration]))
                output.append(row)
    else:
        outputRow.append("Pick up 1 card")
        outputRow.append(str(rules[3]))
        output.append(outputRow)
    return output
# WRITES CSV FILE AND RUNS AS MANY LINES AS WANTED CURRENTLY SET TO 1000

def outputter():
    with open('illegalMoves.csv','w',newline='') as file:
        writer = csv.writer(file)
        i=0
        startline = ["Card on the Table: "," Cards in Hand: "," Possible Move: "," Applicable rule: "]
        writer.writerow(startline)
        # HOW MANY PLAYS TO GENERATE (ANYWHERE BETWEEN 1 AND 7 OPTIONS PER PLAY)
        for i in range(numberrun):
            newlines = playmaker()
            writer.writerows(newlines)
                
                    

def outputText():
    with open('illegaltextmoves.txt','a+') as file:
        table = "Card on the table: "
        hand = ", Cards in your hand: "
        move = ", You could play: "
        rule = ", because: "
        end = "\n"
        for i in range(numberrun):
            newline = playmaker()
            for moves in newline:
                outputline = table + moves[0] + hand + moves[1] + move + moves[2] + rule +moves[3]+end
                file.write(outputline)

def outputAltText():
    with open('illegalmovestext.txt','a+') as file:
        table = ""
        hand = " ; "
        move = " ; "
        rule = " ; "
        end = "\n"
        for i in range(numberrun):
            newline = playmaker()
            for moves in newline:
                outputline = table + moves[0] + hand + moves[1] + move + moves[2] + rule +moves[3]+end
                file.write(outputline)

def shuffler(array):
    random.shuffle(array)
    return array

def illegalmover(array):
    illegalmove =[]
    # card on the table in readable format
    table = array[0]
    # card in hand in readable format
    hand = array[1]
    # spllit up the hand into individual cards
    handcards = hand.split(",")
    # randomly select card from hand
    rand = random.randint(0,6)
    newcard = handcards[rand]
    # check for why illegal
    tableparts = table.split(" ")
    trycard = newcard.split(" ")

    #  Rejoins card types into single string
    if trycard[2] == "Draw":
        typecard = trycard[2] +" "+ trycard[3]
    else:
        typecard = trycard[2]
    
    if tableparts[1] == "Draw":
        tabletype = tableparts[1]+" "+tableparts[2]
    else:
        tabletype = tableparts[1]


    if tableparts[0] != trycard[1] and trycard[1] != "Wild" and tabletype != typecard and tableparts[0] != "Wild":
        finaltable = tableparts[0] + " " + tabletype
        # print(finaltable)
        finaltry = trycard[1] + " " + typecard
        # print(finaltry)
        illegalmove.append(str(finaltable))
        illegalmove.append(str(hand))
        illegalmove.append(str(finaltry))
        illegalmove.append(str(rules[8]))
    else:
        print("nothing illegal found yet")

    # print(illegalmove)
    
    return illegalmove     
            
def outputillegals():
    #stuff
    with open('BigDatasetCompleteListOfIllegalMoves.csv','w',newline='') as file:
        writer = csv.writer(file)
        i=0
        startline = ["Card on the Table: "," Cards in Hand: "," Possible Move: "," Applicable rule: "]
        writer.writerow(startline)
        # HOW MANY PLAYS TO GENERATE (ANYWHERE BETWEEN 1 AND 7 OPTIONS PER PLAY)
        for i in range(numberrun):
            newlines = playmaker()
            # illegal move add on down Here vVv
            if i % numberillegal ==0:
                newplay = illegalmover(newlines[0])
                if newplay == []:
                    print("oop")
                else:
                    print(newplay)
                    writer.writerow(newplay)

def outputLegalAndIllegal():
    #tings
    with open('BigDatasetLegalAndIllegal.txt','a+') as file:
        table = ""
        hand = " ; "
        move = " ; "
        rule = " ; "
        end = "\n"
        for i in range(numberrun):
            newline = playmaker()
            for moves in newline:
                outputline = table + moves[0] + hand + moves[1] + move + moves[2] + rule +moves[3]+end
                file.write(outputline)
            if i % numberillegal ==0:
                illegalplay = illegalmover(newline[0])
                if illegalplay ==[]:
                    print("oopsie")
                else:
                    illegaloutputline = table + illegalplay[0] + hand + illegalplay[1] + move + illegalplay[2] + rule + illegalplay[3] +end
                    file.write(illegaloutputline)
                    
                
            


# WORK IN PROGRESS UP HERE

# outputter()
# outputText()
# outputAltText()

outputillegals()
outputLegalAndIllegal()