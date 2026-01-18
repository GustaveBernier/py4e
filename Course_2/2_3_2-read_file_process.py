# Use words.txt as the file name
fname = input("Enter file name: ").strip()
try:
    fh = open(fname)
except:
    print("File not found.")
    quit()

conf_total = 0
conf_count = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    sep = ': '
    isep = line.find(sep)
    conf = float(line[isep+len(sep):].rstrip())
    conf_total = conf_total + conf
    conf_count = conf_count + 1

conf_avg = conf_total / conf_count
print('Average spam confidence:', conf_avg)