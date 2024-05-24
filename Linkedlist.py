class node:
    def _init_(self,data):
        self.data=data
        self.ref=None
class linkedlist:
    def _init_(self):
        self.head=None
## travesing a linked list        
    def print_ll(self):
        if self.head==None:
            print("linked list is empty")
        else:
            next=self.head
            while next != None:
                print(next.data,end="-->")
                next=next.ref

##adding node at begining
    def addat_begining(self,data):
        obj1=node(data)
        obj1.ref=self.head
        self.head=obj1

##adding node at end
    def addat_end(self,data):
        obj1=node(data)
        if self.head == None:
            self.head=obj1
        else:
            next=self.head
            while next.ref != None:
                next=next.ref
            next.ref=obj1   

## adding at specific position
##    def addat_specific_position(self,pos,data):
        
        




obj1=linkedlist()
o1=node(30)
o2=node(40)
o3=node(40)
o4=node(60)
o5=node(70)
o6=node(80)
obj1.head=o1
o1.ref=o2
o2.ref=o3
o3.ref=o4
o4.ref=o5
o5.ref=o6
o6.ref=None
obj1.addat_begining(20)
obj1.addat_begining(10)
obj1.addat_end(90)
obj1.print_ll()
