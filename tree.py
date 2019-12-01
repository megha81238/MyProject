class node:
	
	def __init__(self, data=None):
		self.data=data
		self.left=None
		self.root.right=None

class binarySearchTree:
	def __init__(self):
		self.root=None

	def insert(self,data):
		ptr=node(data)
		self.root=node()
		if self.root==None:
			self.root=ptr
		else:
			while self.root.data!= None:
				if ptr.data>self.root.data:
					if self.root.right==None:
						self.root.right=ptr
					else:
						_insert(ptr.data,self.root.right)
				else:
					if self.root.left==None:
						self.root.left=ptr
					else:
						_insert(ptr.data,self.root.left)
		
	def _insert(data,root):
		
			
	

