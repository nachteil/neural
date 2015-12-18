import csv


def getReader(fname):
    f = open(fname, "r")
    reader = csv.reader(f)
    return reader


base = "outs/out_{0}.csv"
readers = []

for i in range(1, 25):
    readers.append(getReader(base.format(i)))

errs = [[] for i in range(0,201)]
devs = [[] for i in range(0,201)]

for reader in readers:
    i = 0
    for row in reader:
        if i < 200:
           errs[i].append(float(row[1]))
           devs[i].append(float(row[2]))
           i += 1

for e in range(0,202):
    print "{0},{1},{2}".format(e, sum(errs[e])/len(errs[e]), sum(devs[e])/len(devs[e]))
