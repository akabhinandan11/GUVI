s12,s22=input().split()
s=0
if len(s12)>len(s22):
    s12,s22=s22,s12
q=0
while q<len(s12):
    s+=(ord(s22[q])-ord(s12[q]))
    q+=1
for q in range(q,len(s22)):
    s+=ord(s22[q])-ord('a')+1
print(s)
