import os, random, time
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
    train1 = Train(random.randrange(25), random.randrange(20))
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

starttime = time.monotonic()
while True:
    main()
    time.sleep(1.0 - ((time.monotonic() - starttime) % 1.0))