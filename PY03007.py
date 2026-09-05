import sys
data = sys.stdin.read().split()
initiation = True
idx = 0
line = []
while idx < len(data):
    word = data[idx].lower()
    if initiation:
        word = word.title()
        initiation = False
    if word[-1] in ('.', '?', '!'):
        initiation = True
        print(' '.join(line), word[:-1])
        line.clear()
    else:
        line.append(word)
    idx+=1
        