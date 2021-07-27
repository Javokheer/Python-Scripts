#! python3


"""returns words with their number of occurences"""
handle = open('sort.txt')
dic = {}
lst = []
for line in handle:
    words = line.split()
    for word in words:
        dic[word] = dic.get(word, 0) + 1
for (k, v) in dic.items():
    newtup = (v, k)
    lst.append((newtup))
sort = sorted(lst, reverse=True)
for ele, ment in sort[:10]:
    print(ment, ele)
    
    
    