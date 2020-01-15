listMain = []
if __name__ == '__main__':
    N = int(input())
for x in range(N):
    comm = input()
    listOfComm = comm.split()
    if(listOfComm[0]=='insert'):
        listMain.insert(int(listOfComm[1]),int(listOfComm[2]))
    elif(listOfComm[0]=='sort'):
        listMain.sort()
    elif(listOfComm[0]=='print'):
        print(listMain,end='\n')
    elif(listOfComm[0]=='remove'):
        for no in listMain:
            if(no==int(listOfComm[1])):
                listMain.remove(no)
                break
    elif(listOfComm[0]=='append'):
        listMain.append(int(listOfComm[1]))
    elif(listOfComm[0]=='pop'):
        listMain.remove(listMain[len(listMain)-1])
    elif(listOfComm[0]=='reverse'):
        listMain.reverse()
    

