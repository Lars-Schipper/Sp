infile = open('opdracht_8.txt', 'r')
lines = infile.readlines()
infile.close()

lines = [line.replace(' ','')for line in lines]
lines = [line.replace('\n','')for line in lines]

outfile = open('opdracht_8.txt', 'w')
outfile.writelines(lines)
