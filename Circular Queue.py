class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
    def Display(self):
        print(self.data)

    def Get_Data(self):
        return self.data

class Circular_Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def Enqueue(self,node):
        if self.head is None:
            self.head = node
            self.tail = node
            self.tail.next = self.head
            self.size = self.size + 1
        else:
            self.tail.next = node
            self.tail = node
            self.tail.next = self.head
            self.size = self.size + 1

    def Dequeue(self):
        if self.head is None:
            print('This Queue is Empty')
            return
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size = self.size - 1
            return
        else:
            Current = self.head
            self.head = self.head.next
            Current = None
            self.tail.next = self.head
            self.size = self.size - 1

    def Is_Empty(self):
        if self.size == 0:
            print('Circular Queue is Empty')
        else:
            print('Circular Queue is not empty')
            
    def Size(self):
        if self.size == 0:
            print('Circular Queue is Empty')
        else:
            print("the size of your queue is: ", self.size)

    def Search_Value(self,value):
        if self.head.Get_Data() == value:
            print('The value is present in circular queue')
            return
        current = self.head.next
        while current != self.head:
            if value == current.Get_Data():
                print('The value is present in Circular Queue')
                return  
            current = current.next
        print('The value is not present in Circular Queue')

    def Display_Values(self):
        if self.head == None:
            print('Circular Queue is Empty')
            return
        self.head.Display()
        current = self.head.next
        while current != self.head:
            current.Display()
            current = current.next
        self.head.Display()

Queue = Circular_Queue()
Queue.Enqueue(node(12))
Queue.Enqueue(node(45))
Queue.Enqueue(node(17))
Queue.Enqueue(node(25))
Queue.Dequeue()
Queue.Size()
Queue.Search_Value(3)
Queue.Display_Values()
