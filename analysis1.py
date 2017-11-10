import collections
fp = open('hashes.orig')
List = []
collision = []
result = []
print 'Collision in hashes.orig'
while 1:
    line = fp.readline()
    line = line.split('  ')[0]
    List.append(line)
    if not line:
        break
collision = [item for item, count in collections.Counter(List).items() if count > 1 ]
for element in collision:
    print str(element) +' ocours '+ str(List.count(element))


# collision between .alt and .orig
print 'collision between .alt and .orig'

fp = open('hashes.alt')
List = []
collision = []
result = []
while 1:
    line = fp.readline()
    line = line.split('  ')[0]
    List.append(line)
    if not line:
        break
collision = [item for item, count in collections.Counter(List).items() if count > 1 ]
for element in collision:
    print str(element) +' ocours '+ str(List.count(element))
