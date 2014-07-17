class node(object):
    def __init__(self,value,children=[]):
        self.value=value
        self.children=children

    def __repr__(self,level=0):
        ret="\t"*level+self.value+"\n"
        for child in self.children:
            ret+=child.__repr__(level+1)
        return ret

tree = node("grandmother", [
    node("daughter", [
        node("granddaughter"),
        node("grandson")]),
    node("son", [
        node("granddaughter"),
        node("grandson")])
    ]);

print tree


class Bst(object):
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right
    def search(self,value):
        if self.value==value:
          return True
        elif value<self.value:
          if self.left!=None:
            return self.left.search(value)
          else:
            return False
        else:
          if self.right!=None:
            return self.right.search(value)
          else:
            return False
    def insert(self,value):
        if self.value==value:
          return
        elif value<self.value:
          if self.left!=None:
            self.left.insert(value)
          else:
            self.left=Bst(value)
        else:
          if self.right!=None:
            self.right.insert(value)
          else:
            self.right=Bst(value)

    def inorder(self):
        if self.left!=None:        
          self.left.inorder()
        print self.value
        print " "
        if self.right!=None:        
          self.right.inorder()

    def preorder(self):
        print self.value
        print " "        
        if self.left!=None:        
          self.left.preorder()
        if self.right!=None:        
          self.right.preorder()

    def postorder(self):           
        if self.left!=None:        
          self.left.postorder()
        if self.right!=None:        
          self.right.postorder()
        print self.value
        print " " 


    def lca(self,value1,value2):
        if self.value==None:
          return -1
        if (value1>=self.value and value2<=self.value) or (value1<=self.value and value2>=self.value):
          print "hi"
          return self.value
        elif value1>self.value and value2>self.value:
          print "hi1"
          return self.right.lca(value1,value2)
        else:
          print "hi2"
          return self.left.lca(value1,value2)

    def inorderlist(self):
        ret=[]
        if self.left!=None:        
          leftlist=self.left.inorderlist()
          ret.extend(leftlist)
        ret.append(self.value)
        if self.right!=None:        
          rightlist=self.right.inorderlist()
          ret.extend(rightlist)
        return ret
    
    def zigzag(self):
        stack1=[]
        stack2=[]
        stack=[]
        print self.value
        stack.append(self.value)
        stack1=self.travlr() 
        while (len(stack1) or len(stack2)):
          while len(stack1):
              s=stack1.pop()
              print s.value
              stack.append(s.value)
              #stack2.extend(s.travrl())
              if s.right!=None:
                stack2.append(s.right)
              if s.left!=None:
                stack2.append(s.left)
          while len(stack2):
              s=stack2.pop()
              print s.value
              stack.append(s.value)
              #stack1.extend(s.travlr())
              if s.left!=None:
                stack1.append(s.left)
              if s.right!=None:
                stack1.append(s.right)
        return stack

    

    def travlr(self):
        stack=[]
        if self.left!=None:
          stack.append(self.left)
        if self.right!=None:
          stack.append(self.right)
        return stack
    def travrl(self):
        stack=[]
        if self.right!=None:
          stack.append(self.right)
        if self.left!=None:
          stack.append(self.left)
        return stack
    
    def levelordertrav(self):
        queue=[self]     
        while len(queue):
             queue1=[]
             l=len(queue)
             for i in xrange(l):
                item=queue.pop(0)
                queue1.append(str(item.value))
                if item.left!=None:
                  queue.append(item.left)
                if item.right!=None:
                  queue.append(item.right)
             print ' '.join(queue1)        

    
    def dfs(self):
        ret=[]
        if self.left!=None:
          ret=self.left.dfs()
        if self.right!=None:
          ret.extend(self.right.dfs())
        #print self.value
        ret.append(self.value)
        return ret 

root=Bst(10)
root.insert(5)
root.insert(3)
root.insert(4)
root.insert(23)
root.insert(13)
root.insert(10)
root.insert(1)
print "INORDER"
root.inorder()
print "PREORDER"
root.preorder()
print "POSTORDER"
root.postorder()   

print root.lca(13,4)
print root.lca(1,5)

l=root.inorderlist()
print l
           
print "ZIGZAG"  
print root.zigzag()

print "LEVEL ORDER TRAVERSAL"
root.levelordertrav()

print root.dfs()








                  






          





