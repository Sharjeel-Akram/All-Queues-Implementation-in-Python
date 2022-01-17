class Node:
    def __init__(self,Job,Priority):
        self.Job = Job
        self.Priority = Priority
        self.next = None

    def Display(self):
        print('Job name:',self.Job,',','Priority:',self.Priority)
        
    def Get_Job(self):
        return self.Job

class Job_Priority:
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
        if self.head.Get_Job() == value:
            print('The value is present in Priority queue')
            self.head.Display()
            return
        current = self.head
        while current != None:
            if value == current.Get_Job():
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

    def Menu(self):
        print('a = Enqueue (add a Job in the Priority Queue))')
        print('b = Dequeue (delete a Job from the Priority Queue))')
        print('c = Size (print number of jobs currently present in the Priority Queue)')
        print('d = Search a Job (on the basis of Name)')
        print('e = Display Priority Queue')
        print('f = Exit (stop the program)')
        Do = input("Please Press S to start the program: ")
        while Do != "f":
            choice = input('Please select your Choice from above and enter here: ')
            if choice == 'a':
                loop = input("enter how many time you want to insert node: ")
                for i in range(int(loop)):
                    Job = input('Enter name of the Job:')
                    Priority = int(input('Enter priority for Job: '))
                    Queue.Enqueue(Node(Job,Priority))
                Queue.Display_Values()
            elif choice == 'b':
                Queue.Dequeue()
                print('After Deletion:')
                Queue.Display_Values()
            elif choice == 'c':
                Queue.Size()
            elif choice == 'd':
                Job = input("Enter Job you want to search: ")
                Queue.Search_Value(Job)
            elif choice == 'e':
                Queue.Display_Values()
            elif choice == 'f':
                print('Program is Finished.')
                break
Queue = Job_Priority()
Queue.Menu()

