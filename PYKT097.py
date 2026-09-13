import sys
input = sys.stdin.readline
def get_sentence(x, ch):
    sentence = ''.join(tmp).strip() + ch
    words = sentence.split()
    words[0] = words[0].title()
    return ' '.join(words)
line = input()
s = []
while line:
    tmp = []
    for ch in line.lower().strip():
        if ch in ('.', '?', '!'):
            s.append(get_sentence(tmp, ch))
            tmp.clear()
        else:   tmp.append(ch)
    if tmp:
        s.append(get_sentence(tmp, '.'))
    line = input()
print(*s, sep = '\n')