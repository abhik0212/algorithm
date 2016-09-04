def check_interleave(A,B,C):
	l1,l2,l3=len(A),len(B),len(C)
	i=j=k=0
	if not(l1+l2==l3):
		return 0
	S=[[0 for y in xrange(l2+1)] for x in xrange(l1+1)]
	S[0][0]=1
	for i in xrange(1,l1+1):
		if A[i-1]==C[i-1]:
			S[i][0]=S[i-1][0]
	for j in xrange(1,l2+1):
		if B[j-1]==C[j-1]:
			S[0][j]=S[0][j-1]
	
	for i in xrange(1,l1+1):
		for j in xrange(1,l2+1):
			#print i,j,S
			if (A[i-1]==C[i+j-1] and not(B[j-1]==C[i+j-1])):
				S[i][j]=S[i-1][j]
			elif (not(A[i-1]==C[i+j-1]) and B[j-1]==C[i+j-1]):
				S[i][j]=S[i][j-1]
			elif A[i-1]==C[i+j-1] and B[j-1]==C[i+j-1]:
				S[i][j]=S[i][j-1] or S[i-1][j]
	#print S
	return S[l1][l2]

if __name__=='__main__':
	A="xyz"
	B="xab"
	C="xaxyzb"
	#print check_interleave(A,B,C)
	#print check_interleave("XXY", "XXZ", "XXZXXXY")
	#print check_interleave("XY" ,"WZ" ,"WZXY")
	print check_interleave("XY", "X", "XXY")
	print check_interleave("YX", "X", "XXY")
	print check_interleave("XXY", "XXZ", "XXXXZY");
