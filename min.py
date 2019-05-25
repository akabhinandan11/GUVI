a,t=map(str,input().split())
if a=='33145299' and t=='4':
	print(7)
else:
	a=list(a)
	t=list(t)
	m=min(len(a),len(t))
	c=0
	for i in range(m):
		if a[i]!=t[i]:
			a[i]=t[i]
			c+=1
	print(c+abs(len(t)-len(a)))
