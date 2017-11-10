fp = open('hashes.orig')
f = open("3.txt","w+")
result = []
i = 0
while i < 1000:
    line = fp.readline()
    line = line.split('  ')[0]
    result.append(bin( int(line, 16)))
    binary = result[i]
    result[i] = binary[2:].zfill(32)
    i += 1
i = 0
while i < 32:
    k = 0
    cal1s = 0
    while k < 1000:
        if(result[k][i] == '1'):
            cal1s += 1
        k += 1
    print 'Column: ' + str(i) + ' of 1s ratio is ' + str(float(cal1s)/1000)
    f.write(str(float(cal1s)/1000)+'\n')
    i += 1
