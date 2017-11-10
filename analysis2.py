import collections
fp = open('hashes.orig')
result = []
sum = 0.0
i = 0
while i < 1000:
    line = fp.readline()
    line = line.split('  ')[0]
    result.append(line)
    if not line:
        break
i = 0
while i < 1000:
    result[i] = bin( int(result[i],16))
    i += 1
i = 0
while i < 1000:
    binary = result[i]
    #print binary[2:].zfill(32)
    friquency = binary[2:].count('1')
    result[i] = float(friquency)/32
    print 'org.'+str(i)+' ratio of 1s to 0s is: '+str(result[i])
    sum += result[i]
    i += 1
print 'Totally ration of 1s to 0s: '+ str(sum/1000) + ', '+ str(1-sum/1000)
