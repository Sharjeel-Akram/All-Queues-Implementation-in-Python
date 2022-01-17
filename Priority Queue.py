class Node:
    def __init__(self, data, Priority):
        self.data = data
        self.Priority = Priority
        self.next = None

    def Display(self):
        print('Data',self.data,',','Priority',self.Priority)

    def Get_Data(self):
        return self.data
    
class Priority_Queue:
    def __init__(self):
        self.head = None
        self.size = 0

    def Enqueue(self,node):
        if self.head is None:
            self.head = node
            self.size = self.size + 1
        elif node.Priority > self.head.Priority:
            node.next = self.head
            self.head = node
            self.size = self.size + 1
        else:
            current = self.head
            Temp = None
            while (current!= None) and (current.Priority > node.Priority):
                Temp = current
                current = current.next
            node.next = current
            Temp.next = node
            self.size = self.size + 1 

    def Dequeue(self):
        if self.head is None:
            print("The Queue is Empty.")
            return
        current  = self.head
        self.head = self.head.next
        current = None
        self.size = self.size - 1

    def Is_Empty(self):
        if self.size == 0:
            print('Priority Queue is Empty')
        else:
            print('Priority Queue is not empty')

    def Size(self):
        if self.size == 0:
            print('Priority Queue is Empty')
        else:
            print("the size of your queue is: ", self.size)

    def Search_Value(self,value):
        if self.head.Get_Data() == value:
            print('The value is present in Priority queue')
            self.head.Display()
            return
        current = self.head
        while current != None:
            if value == current.Get_Data():
                print('The value is present in Priority Queue')
                current.Display()
                return  
            current = current.next
        print('The value is not present in Priority Queue')
        

    def Display_Values(self):
        if self.head == None:
            print('Priority Queue is Empty')
            return
        current = self.head
        while current != None:
            current.Display()
            current = current.next

Queue = Priority_Queue()
Queue.Enqueue(Node(1,0))
Queue.Enqueue(Node(12,23))
Queue.Enqueue(Node(23,34))
Queue.Enqueue(Node(9,14))
Queue.Enqueue(Node(10,2))
Queue.Enqueue(Node(4,67))
Queue.Dequeue()
Queue.Display_Values()
Queue.Search_Value(10)
Queue.Size()
Queue.Is_Empty()


