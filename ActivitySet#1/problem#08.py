# Files

filename = "dataset/mbox-short.txt"
fhand=open(filename)
num=""
for line in fhand:
  if line.startwith("X-DSPAM-Confidence:"):
    print(line)
