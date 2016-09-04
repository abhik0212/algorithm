def kadane(lst):
	g_max=c_max=0
	c_start=c_end=g_start=g_end=0
	for i,elem in enumerate(lst):
		c_max=max(c_max+elem,elem)
		if c_max==elem:
			c_start=c_end=i
		else:
			c_end=i
		if c_max>g_max:
			g_max,g_start,g_end=c_max,c_start,c_end		
	return g_max,g_start,g_end

def maxsubmatrix(matrix,row,col):
	max_global=0
	pos_left=pos_right=pos_up=pos_down=0
	for left in xrange(col):
		temp=[0 for x in xrange(row)]
		for right in xrange(left,col):
			for i in xrange(row):
				temp[i]+=matrix[i][right]
			max_current,up_current,down_current=kadane(temp)
			print left,right,"\t",max_current,up_current,left,down_current,right
			if max_current > max_global:
				max_global,pos_left,pos_right,pos_up,pos_down=max_current,left,right,up_current,down_current
	print max_global,pos_up,pos_left,pos_down,pos_right

m=[[1, 2, -1, -4, -20],[-8, -3, 4, 2, 1],[3, 8, 10, 1, 3],[-4, -1, 1, 7, -6]]
maxsubmatrix(m,4,5)
#l=[4, -2, -8, 5, -2, 7, 7, 2, -6, 5]
l=[4, -2, -8, 5, -2, 7, 7, 2, -6, 5]
print kadane(l)
#print mssl(l)
