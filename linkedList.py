class node:
    def __init__(self,data=None):
        self.data=data
        self.link=None
        

class linkedlist:
    def __init__(self):
        self.start=node()
        self.start=None
        
         
    #insertion at the end
    
    def insert(self,data):
        n=node(data)
        n.data=data
        n.link=None
        if self.start==None:
            self.start=n
        else:
            ptr=node()
            ptr=self.start
            while ptr.link!=None:
                ptr=ptr.link
            ptr.link=n
     
    #insertion at the begining
    
    def insert_beg(self,data):
        n=node(data)
        n.data=data
        n.next=None
        if self.start==None:
            self.start=n
        else:
            n.link=self.start
            self.start=n
    
    #insert element at given position
    
    def insert_bet(self,data):
        n=node(data)
        n.data=data
        n.link=None
        if self.start==None:
            self.start=n
        else:
            ele=int(input("enter the element after which data is to be inserted"))
            loc=node()
            loc=self.start
            while loc.data!=ele:
                loc=loc.link
            n.link=loc.link
            loc.link=n
