import sys
st = sys.argv[1]
result = []


def getanagram(prefix, word):
    length = len(word)
    if length == 0:
        result.append(prefix)
    else:
        for i in range(0, length):
            getanagram(prefix+word[i], word[0:i]+word[i+1:length])
    return result

if len(st) != "":
    res = getanagram("", st)
    res.sort()
    out = open("anagram_out.txt","w")
    for l in res:
        out.write(l+"\n")