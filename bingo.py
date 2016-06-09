from random import *
def card():
    cnum = 25
    
    card = []
    
    count = 1
    
    while cnum != 0:
        if count < 6:
            card.append("B" + str(randrange(1,16)))
            count = count + 1
            cnum = cnum - 1
        elif count > 5 and count < 11:
            card.append("I" + str(randrange(16,31)))
            count = count + 1
            cnum = cnum - 1
        elif count > 10 and count < 16:
            card.append("N" + str(randrange(31,46)))
            count = count + 1
            cnum = cnum - 1
        elif count > 15 and count < 21:
            card.append("G" + str(randrange(46,61)))
            count = count + 1
            cnum = cnum - 1
        elif count > 20 and count < 26:
            card.append("O" + str(randrange(61,76)))
            count = count + 1
            cnum = cnum - 1       
        else:
            break
    
    return card
    
    # Generates card
def winningcard():
    
    calls = ["B1","B2","B3","B4","B5","B6","B7","B8","B9","B10","B11","B12","B13","B14","B15","I16","I17","I18","I19","I20","I21","I22","I23","I24","I25","I26","I27","I28","I29","I31","N32","N33","N34","N35","N36","N37","N38","N39","N40","N41","N42","N43","N44","N45","G46","G47","G48","G49","G50","G51","G52","G53","G54","G55","G56","G57","G58","G59","G60","O61","O62","O63","O64","O65","O66","O67","O68","O69","O70","O71","O72","O73","O74","O75"]
    
    shuffle(calls)
    
    new = [calls[0],calls[1],calls[2],calls[3],calls[4]]
    return new
    
# Generate winning numbers.
def main(card):
    options = winningcard()
    newcard = []
    for i in card:
        if i == options[0] or i == options[1] or i == options[2] or i == options[3] or i == options[4]:
            newcard.append(i[0] + '0')
        else:
            newcard.append(i)
            
    newcard = sorted(newcard)
    times = 0
    winner = False
    while winner != True:
        l1d = newcard[0] + newcard[1] + newcard[2] + newcard[3] + newcard[4]
        l2d = newcard[5] + newcard[6] + newcard[7] + newcard[8] + newcard[9]
        l3d = newcard[10] + newcard[11] + newcard[12] + newcard[13] + newcard[14]
        l4d = newcard[15] + newcard[16] + newcard[17] + newcard[18] + newcard[19]
        l5d = newcard[20] + newcard[21] + newcard[22] + newcard[23] + newcard[24]

        l1a = newcard[0] + newcard[5] + newcard[10] + newcard[15] + newcard[20]
        l2a = newcard[1] + newcard[6] + newcard[11] + newcard[16] + newcard[21]
        l3a = newcard[2] + newcard[7] + newcard[12] + newcard[17] + newcard[22]
        l4a = newcard[3] + newcard[8] + newcard[13] + newcard[18] + newcard[23]
        l5a = newcard[4] + newcard[9] + newcard[14] + newcard[19] + newcard[24]
        acc1 = newcard[0] + newcard[6] + newcard[12] + newcard[18] + newcard[24]
        acc2 = newcard[4] + newcard[8] + newcard[12] + newcard[16] + newcard[20]
    


        if (l1d == "00000") or (l2d == "00000") or (l3d == "00000") or (l4d == "00000") or (l5d == "00000") or (l1a == "00000") or (l2a == "00000") or (l3a == "00000") or (l4a == "00000") or (l5a == "00000") or (acc1 == "00000") or (acc2 == "00000"):
            
            times = times + 1
            return times
            winner = True
            
        else:
            times = times + 1
            ran = winningcard()
            for i in newcard:
                if i == ran[0] or i == ran[1] or i == ran[2] or i == ran[3] or i == ran[4]:
                    pos = newcard.index(i)
                    newcard[pos] = "0"
                    
                else:
                    winner = False

def sim(timestorun):
    average = 0
    minimum = []
    maximum = []
    times = timestorun
    while times != 0:
        numcard = main(card())
        
        average = average + numcard
        
        minimum.append(numcard)
        maximum.append(numcard)
        times = times - 1
    average = average / timestorun
    print "The maximum number of times is: " + str(max(maximum))
    print "The minimum number of times is: " + str(min(minimum))
    print "The average number of times is: " + str(average) + "."
    

    
    
    
    
#Check card with winning numbers, start at dictionary.
    
print sim(1000)

