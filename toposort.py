class Topsort():

	def __init__(self,l):
		self.dct={}
		self.nodes=set()
		self.visited=set()
		self.stack=[]
		for elem in l:
			src=elem[0]
			dst=elem[1]
			if not(self.dct.has_key(src)):
				self.dct[src]=[dst]
			else:
				self.dct[src].append(dst)
			self.nodes.add(src)
			self.nodes.add(dst)
		print self.dct,self.nodes,self.visited

	def sort(self):
		while len(self.nodes) >len(self.visited):
			remaining=self.nodes - self.visited
			print self.nodes,self.visited,remaining
			node=remaining.pop()
			print "node ",node
			self.topsortutil(node)
		while len(self.stack):
			print self.stack.pop()
		
	
	def topsortutil(self,node):
		self.visited.add(node)
		#get the list of nodes reachable from node
		templ=self.dct.get(node,[])
		for n in templ:
			#if n not already visited,explore it further
			if n not in self.visited:
				self.topsortutil(n)
		#node has been fully explored at this time
		self.stack.append(node)

l=[(2,4),(3,5),(2,5),(5,6),(1,2)]	
tobj=Topsort(l)
tobj.sort()
