import math
from sets import Set
fp = open('hashes.orig')
i = 0
result = []
freqList = []
while i < 1000:
    line = fp.readline()
    line = line.split('  ')[0]
    result.append(bin( int(line, 16)))
    binary = result[i]
    result[i] = binary[2:].zfill(32)
    i += 1
setList = list(Set(result))
print 'hash.org'
print 'Unique string in hash.org are: '+ str(len(setList))
i = 0
collision = []
for uniqeString in setList:
    ctr = 0
    for aString in result:
        if aString == uniqeString:
            ctr += 1
            if ctr >1:
                collision.append(uniqeString)
    freqList.append(float(ctr) / 1000)
    
ent = 0.0
for freq in freqList:
    ent = ent + freq * math.log(freq, 2)
ent = -ent
print 'There are '+ str(len(collision)) + ' collision in hash.org'
print 'Shannon entropy in hash.org is: ' + str(ent)


fp = open('hashes.alt')
i = 0
result = []
freqList = []
setList = []
while i < 2000:
    line = fp.readline()
    line = line.split('  ')[0]
    result.append(bin( int(line, 16)))
    binary = result[i]
    result[i] = binary[2:].zfill(32)
    i += 1
setList = list(Set(result))
print 'hash.alt: '
print 'Unique string in hash.alt are: '+ str(len(setList))
i = 0
collision = []
for uniqeString in setList:
    ctr = 0
    for aString in result:
        if aString == uniqeString:
            ctr += 1
            if ctr >1:
                collision.append(uniqeString)
    freqList.append(float(ctr) / 2000)
    
ent = 0.0
for freq in freqList:
    ent = ent + freq * math.log(freq, 2)
ent = -ent
print 'There are '+ str(len(collision)) + ' collision in hash.alt'
print 'Shannon entropy in hash.alt is: ' + str(ent)
