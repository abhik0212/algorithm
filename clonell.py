class Node(object):
	def __init__(self,value,next=None,random=None):
		self.value=value
		self.next=next
		self.random=random

def printll(head):
	while head:
		print head.value,head.random.value
		head=head.next

def clonell(head):
	head1=head
	#1) Create the copy of node 1 and insert it between node 1 & node 2 in original Linked List, create the copy of 2 and insert it between 2 & 3.. Continue in this fashion, add the copy of N afte the Nth node
	while head1:
		temp=Node(head1.value)
		temp.next=head1.next
		head1.next=temp
		head1=temp.next
	head2=head.next

	#2)Now copy the arbitrary link in this fashion    original->next->arbitrary = original->arbitrary->next
	
	head1=head
	while head1:
		head1.next.random=head1.random.next
		head1=head1.next.next
	
	#3)Now restore the original and copy linked lists in this fashion in a single loop. original->next = original->next->next;    	copy->next = copy->next->next;
	#4) Make sure that last element of original->next is NULL.

	head1=head
	copy=head1.next
	while True:
		head1.next=head1.next.next
		head1=head1.next
		if head1==None:
			break
		copy.next=copy.next.next
		copy=copy.next
	return head2

if __name__=='__main__':
	node1,node2,node3,node4,node5=Node(1),Node(2),Node(3),Node(4),Node(5)
	node1.next=node2
	node2.next=node3
	node3.next=node4
	node4.next=node5
	node1.random=node3
	node2.random=node1
	node3.random=node5
	node4.random=node3
	node5.random=node2
	print node1
	printll(node1)
	head2=clonell(node1)
	print node1
	printll(node1)
	print head2
	printll(head2)
	
