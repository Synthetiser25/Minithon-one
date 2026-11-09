import os
from train import Train
rows, cols = (25, 25)
mat = [["." for j in range(rows)] for i in range (cols)]
trains = []

def reprint():
    os.system("clear")
    for i in range(rows):
        for j in range(cols):
            print(" " + mat[i][j] + " ", end="")
        print("\n")

def main():
    train1 = Train(13, 5)
    trains.append(train1)
    print(train1)
    updateMat()
    #reprint()

def updateMat():
    for i in trains:
        segmenting = i.segments
        for j in segmenting:
            mat[j[1]][j[2]] = j[0]
    reprint()

main()