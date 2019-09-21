input_file = "simple.txt"

filereader = open(input_file, 'r')

for row in fileraeader:
    print(row.strip())
    
filereader.close()