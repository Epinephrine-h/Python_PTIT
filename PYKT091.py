from collections import Counter
with open("VANBAN.in") as f:
    words = f.read().split()
    palindromes = [w for w in words if w == w[::-1]]
    cnt = Counter(palindromes)
    max_len = len(max(palindromes, key=len))
    best_words = dict.fromkeys(w for w in palindromes if len(w) == max_len)
    for w in best_words:   print(w, cnt[w])

