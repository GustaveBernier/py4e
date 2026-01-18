# Use words.txt as the file name
fname = input("Enter file name: ").strip()
try:
    fh = open(fname)
except:
    print("File not found.")
    quit()

for line in fh:
    line = line.upper().rstrip()
    print(line)