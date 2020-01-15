import numpy

strDim = []
strDim = input().split()
#print(strDim)
intDim = []
intDim.append(int(strDim[0]))
intDim.append(int(strDim[1]))
#print(intDim)

strMat = []
for a in range(intDim[0]):
    strMat.append(input().split())
#print(strMat)

intMat = []

for a in range(intDim[0]):
    for b in range(intDim[1]):
        intMat.append(int(strMat[a][b]))
#print(intMat)

arrMat = numpy.array(intMat)
arrMat.shape = (intDim[0],intDim[1])
print(numpy.transpose(arrMat))

print(arrMat.flatten())