text = "X-DSPAM-Confidence:    0.8475"
sep = ':'
isep = text.find(sep)
snum = text[isep+1:]
snum.strip()
fnum = float(snum)
print(fnum)