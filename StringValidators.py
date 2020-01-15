if __name__ == '__main__':
    s = input()

alnumCheck = False
alphaCheck = False
digitCheck = False
upperCheck = False
lowerCheck = False

for x in range(len(s)):
    listOfEl = list(s)
    for y in listOfEl:
        if(y.isupper()):
            upperCheck = True
            break
    for y in listOfEl:
        if(y.islower()):
            lowerCheck = True   
            break
    for y in listOfEl :
        if(y.isalpha()):
            alphaCheck = True
            break
    for y in listOfEl :
        if(y.isdigit()):
            digitCheck = True
            break
    if(alphaCheck or digitCheck):
        alnumCheck = True
        break



print(alnumCheck)
print(alphaCheck)
print(digitCheck)
print(lowerCheck)
print(upperCheck)
