import math
from sets import Set
fp = open('hashes.alt')
f = open("4.txt","w+")
orig = []
alt = []
i = 0
while i < 1000:
    line = fp.readline()
    line = line.split('  ')[0]
    orig.append(bin( int(line, 16)))
    binary = orig[i]
    orig[i] = binary[2:].zfill(32)
   

    line = fp.readline()
    line = line.split('  ')[0]
    alt.append(bin( int(line, 16)))
    binary = alt[i]
    alt[i] = binary[2:].zfill(32)
    i += 1
i = 0
sum = 0
while i < 1000:
    diff = 0
    k = 0
    while k < 32:
        if(orig[i][k] != alt[i][k] ):
            diff += 1
        k += 1
    f.write(str(diff)+'\n')
    #print 'filenumber(index): '+ str(i) +' of ' + str(diff) + 'differnces'
    sum += diff
    i += 1
print 'The average differences is :'+str(float(sum/1000))
