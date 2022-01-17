class Node:
    def __init__(self, Roll_Number, Year, Semester, Email):
        self.Roll_Number = Roll_Number
        self.Year = Year
        self.Semester = Semester
        self.Email = Email
        self.next = None

    def Display(self):
        print('Roll Number.:',",",self.Roll_Number,",",'Year:',self.Year,",",'Semester:',self.Semester,",",'Email:',self.Email)

    def Get_RollNumber(self):
        return self.Roll_Number

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
        if self.head.Get_RollNumber() == value:
            print('The value is present in circular queue')
            self.head.Display()
            return
        current = self.head.next
        while current != self.head:
            if value == current.Get_RollNumber():
                print('The value is present in Circular Queue')
                current.Display()
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

    def Menu(self):
        print('a = Enqueue (add a student in the Circular Queue)')
        print('b = Dequeue (delete an element from the Circular Queue)')
        print('c = Size (print number of elements in the Circular Queue)')
        print('d = Search a Student (on the basis of roll number)')
        print('e = Display Circular Queue')
        print('f = Exit (stop the program)')
        Do = input("Please Press S to start the program: ")
        while Do != "f":
            Choice = input('Please select your Choice from above and enter here: ')
            if Choice == 'a':
                loop = input("enter how many time you want to insert node: ")
                for i in range(int(loop)):
                    Roll_Number = int(input('Enter Roll_Number of student:'))
                    Year = int(input('Enter Year of student:  '))
                    Semester = input('Enter Semester of student:')
                    Email = input('Enter Email of student:')
                Queue.Enqueue(Node(Roll_Number,Year,Semester,Email))
                Queue.Display_Values()
            elif Choice == 'b':
                Queue.Dequeue()
                print('After Deletion')
                Queue.Display_Values()
            elif Choice == 'c':
                Queue.Size()
            elif Choice == 'd':
                value = int(input('Enter Roll Number to search: '))
                Queue.Search_Value(value)
            elif Choice == 'e':
                Queue.Display_Values()
            elif Choice == 'f':
                print('Program is Finished')
                break

Queue = Circular_Queue()
Queue.Menu()

