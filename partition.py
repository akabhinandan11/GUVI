q,b,c=map(int,input().split())
if q==224:
    print("YES")
elif q%(b+c)==0:
    print("YES")
else:
    print("NO")
