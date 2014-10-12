"""
These are some methods for reading and
parsing files.
"""

def funcread(fname)
f = open(fname,'r')
for line in f:
    lines = line.split()
    if int(lines[1])>int(lines[2]):
        print 'YES'
    else:
        print 'NO'


funcread('data1.txt')

