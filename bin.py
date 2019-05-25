from itertools import combinations
q,k=map(int,input().split())
a=len(str(q))
listval=list(combinations(str(q),a-k))
listval=sorted(listval)
print("".join(listval[0]))
