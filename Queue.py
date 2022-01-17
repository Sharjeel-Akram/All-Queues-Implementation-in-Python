class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def Display_Nodes(self):
        print("The node in Queue is: ", self.data)

class Queue:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def Enqueue(self,node):
        if self.head == None:
            self.head = node
            self.size = self.size + 1 
            return
        else:
            Temp = self.head
            while Temp.next != None:
                Temp = Temp.next
            Temp.next = node
            self.size = self.size + 1
        
    def Dequeue(self):
        if self.head == None:
            print("Your Queue is empty")
            return
        else:
            temp = self.head
            self.head = self.head.next
            temp = None
            self.size = self.size - 1

    def Is_Empty(self):
        if self.size == 0:
            print("your Queue is empty")
        else:
            print("your Queue is having some values")
            
    def Size(self):
        print("The size of your Queue is: ", self.size)
        
    def Print_Queue(self):
        if self.head == None:
            print("Your Queue is empty")
        Temp = self.head
        while Temp != None:
            Temp.Display_Nodes()
            Temp = Temp.next
        
queue = Queue()
queue.Enqueue(Node(10))
queue.Enqueue(Node(11))
queue.Enqueue(Node(20))
queue.Enqueue(Node(100))
queue.Enqueue(Node(200))
queue.Print_Queue()
queue.Dequeue()
queue.Dequeue()
print("After Deletetion")
queue.Print_Queue()
queue.Size()
queue.Enqueue(Node(30))
queue.Print_Queue()
queue.Is_Empty()
