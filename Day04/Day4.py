file = open("p:/ScriptHub/Scripts/Python/AdventOfCode/Day4Input.txt", "r")

wordSearch = file.read().split()
countOfXMAS = 0

def SearchLine(forward: bool, array: list):
    global countOfXMAS
    xFound = False
    mFound = False
    aFound = False
    sFound = False
    for line in array:
        print("New Line!")
        for char in line:
            match(char):
                case 'X':
                    #Forward
                    if(forward and xFound and ( mFound or aFound or sFound)):
                        print("Found an X out of order; Continuing")
                        xFound = False
                        mFound = False
                        aFound = False
                        sFound = False
                        continue
                    elif (forward):
                        print("Found an X!")
                        xFound = True
                        continue
                    elif(forward == False and sFound and aFound and mFound):
                        print("Found an SAMX!")
                        xFound = True
                        print("Adding one to XMAS counter")
                        #We found an XMAS, reset our search
                        countOfXMAS = countOfXMAS + 1
                        xFound = False
                        mFound = False
                        aFound = False
                        sFound = False
                    else:
                        xFound = False
                        mFound = False
                        aFound = False
                        sFound = False
                case 'M':
                    #Forward
                    if (forward and xFound and not mFound):
                        print("Found an XM!")
                        mFound = True
                        continue
                    if(forward and xFound and mFound):
                        print("Found an XMM; Continuing")
                        xFound = False
                        mFound = False
                        continue
                    #Backward
                    elif (forward == False and sFound and aFound and not mFound):
                        print("Found an SMA!")
                        mFound = True
                        continue
                    if(forward == False and sFound and aFound and mFound):
                        print("Found an SMAA; Continuing")
                        sFound = False
                        mFound = False
                        aFound = False
                        continue
                    else:
                        xFound = False
                        mFound = False
                        aFound = False
                        sFound = False
                        continue
                case 'A':
                    #Forward
                    if(forward and xFound and mFound and not aFound):
                        print("Found an XMA!")
                        aFound = True
                        continue
                    if(forward and xFound and mFound and aFound):
                        print("Found an XMAA; Continuing")
                        xFound = False
                        mFound = False
                        aFound = False
                        continue
                    #Backwards
                    elif (forward == False and sFound and not aFound):
                        print("Found an SA!")
                        aFound = True
                        continue
                    if(forward == False and sFound and aFound):
                        print("Found an SAA; Continuing")
                        sFound = False
                        aFound = False
                        continue
                    else:
                        xFound = False
                        mFound = False
                        aFound = False
                        sFound = False
                        continue
                case 'S':
                    #Forward Behaviour
                    if(forward and xFound and mFound and aFound):
                        print("Found an XMAS!")
                        sFound = True
                        print("Adding one to XMAS counter")
                        #We found an XMAS, reset our search
                        countOfXMAS = countOfXMAS + 1
                        xFound = False
                        mFound = False
                        aFound = False
                        sFound = False
                    #Backwards Behaviour
                    elif (forward == False and sFound and (  aFound or mFound or xFound )):
                        print("Found an S out of order; Continuing")
                        xFound = False
                        mFound = False
                        aFound = False
                        sFound = False
                        continue
                    elif (forward == False):
                        print("Found an S!")
                        sFound = True
                        continue    
                    else:
                        xFound = False
                        mFound = False
                        aFound = False
                        sFound = False
                        continue
                        
                case _:
                    #if we find any other letter than reset
                    xFound = False
                    mFound = False
                    aFound = False
                    sFound = False


def DiagFinder(array, charIndex, lineIndex, forward):
    keyword = ''
    if(forward):
        keyword = 'XMAS'
        resetChar = 'X'
    else:
        keyword = 'SAMX'
        resetChar = 'S'

    currentValue = array[lineIndex][charIndex]
    global countOfXMAS
    #Down->Right Search
    for x in range(1, 4):
        if ((lineIndex + x) >= len(array) or (charIndex + x) >= len(array[lineIndex])):
            print("Current Value: " + currentValue + "; Breaking, no more lines")
            break
        currentValue = currentValue + array[lineIndex + x][charIndex + x]
        print(currentValue)
    if(currentValue == keyword):
        countOfXMAS = countOfXMAS + 1
        print("Found an XMAS searching Down and to the right!")
        return True

    currentValue = resetChar

    #Down->Left Search
    for x in range(1, 4):
        print (x)
        print(lineIndex)
        print(len(array))
        print(charIndex)
        if ((lineIndex + x) >= len(array)):
            print("Current Value: " + currentValue + "; Breaking, no more lines")
            break
        elif((charIndex - x) < 0 ):
            print("Current Value: " + currentValue + "; Breaking, no more characters")
            break
        currentValue = currentValue + array[lineIndex + x][charIndex - x]
        print(currentValue)
    if(currentValue == keyword):
        countOfXMAS = countOfXMAS + 1
        print("Found an XMAS searching Down and to the left!")
        return True

    currentValue = resetChar


    #Up->Right Search
    for x in range(1, 4):
        if ((lineIndex - x) < 0):
            print("Current Value: " + currentValue + "; Breaking, no more lines")
            break
        elif((charIndex + x) >= len(array[lineIndex])):
            print("Current Value: " + currentValue + "; Breaking, no more characters")
            break
        currentValue = currentValue + array[lineIndex - x][charIndex + x]
        print(currentValue)
    if(currentValue == keyword):
        countOfXMAS = countOfXMAS + 1
        print("Found an XMAS searching Up and to the right!")
        return True

    currentValue = resetChar

    #Up->Left Search
    for x in range(1, 4):
        if ((lineIndex - x) < 0):
            print("Current Value: " + currentValue + "; Breaking, no more lines")
            break
        elif((charIndex - x) < 0):
            print("Current Value: " + currentValue + "; Breaking, no more characters")
            break
        currentValue = currentValue + array[lineIndex - x][charIndex - x]
        print(currentValue)
    if(currentValue == keyword):
        countOfXMAS = countOfXMAS + 1
        print("Found an XMAS searching Up and to the left!")
        return True

    currentValue = resetChar

def SearchDiag(array: list):
    for lineIndex, line in enumerate(array):
        for charIndex, char in enumerate(line):
            match(char):
                case 'X':
                    DiagFinder(array, charIndex, lineIndex, forward=True)
                case 'S':
                    DiagFinder(array, charIndex, lineIndex, forward=False)
                    #continue


print("Searching Lines Forward...")
SearchLine(True, wordSearch)
print("Count of Forward Lines: " + str(countOfXMAS))
print("Searching Lines Backward...")
SearchLine(False, wordSearch)
print("Total Count of Lines: " + str(countOfXMAS))
print("Searching Lines Diag...")
SearchDiag(wordSearch)
print("Final Count of XMAS: " + str(countOfXMAS))