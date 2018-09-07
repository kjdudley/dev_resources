s = "ATGCGAAAGCGCGTATTGC"
comp = {"A":"T", "T":"A", "C":"G", "G":"C"}
sc = ""

for i in range(len(s)):
    compbase = comp[s[i]]
    sc = sc[:i] + compbase

sc = sc[::-1]

print(sc)