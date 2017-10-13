import sys
#file_write = open(r"", "w")

#file_read = open(r"C:\Users\ykx\codes\machine-learning\write1.txt", "r")

file_read = open(sys.argv[1], "r")

for line in file_read.readlines():

    if line is None:
        break

    lineList = line.split("\t")

    startPosition = int(lineList[1])
    endPostion    = int(lineList[2])
    chr_name      = lineList[0]


    for i in range(startPosition, endPostion+1):

        chr_str = (chr_name+"\t"+ str(i))
        print(chr_str)


#file_write.close()
file_read.close()