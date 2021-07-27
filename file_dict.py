
"""" opens a file and counts unique string objects in the file """

counts = {}

file = open('test.txt')
for line in file:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
print()
print()

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount == None or count > bigcount:
        bigword = word
        bigcount = count
        
print(bigword, bigcount)

x = ('1', 'sam', 'elon')
print(type(x))