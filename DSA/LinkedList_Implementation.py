class CustomError(Exception):

    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return self.message

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertFirst(self, val):
        n = Node(val)
        if self.head ==  None:
            self.head = n
        else :
            n.next = self.head
            self.head = n
            
    def insertMiddle(self, val, pos):
        if pos == 1 :
            self.insertFirst(val)
            
            
        elif pos < 1  or self.size() < pos+1:
            raise CustomError("Error : Positon doesn't exist")
            
        temp = self.head
        c = 1

        while temp != None and c+1 != pos :
            c += 1
            temp = temp.next

        if temp != None:
            n = Node(val)
            n.next = temp.next
            temp.next = n

    def insertLast(self, val):
        n = Node(val)
        temp = self.head
        
        while temp :
            if temp.next == None :
                break
            temp = temp.next
        
        temp.next = n

    def removeFirst(self):
        if self.head == None :
            print("Nothin to Remove")
            return
        
        temp = self.head.val
        self.head = self.head.next
        return f'{temp} is removed from First'

    def removeMiddle(self, pos):
        
        if self.head == None:
            print("Nothing to remove")
            return
        
        temp = self.head
        c = 2

        if pos == 0 :
            self.removeFirst()
        else:
            while temp != None and c < pos :
                c += 1
                temp = temp.next
            
            if temp.next == None or temp.next == None :
                print("Position not present to remove")
            else :
                temp.next = temp.next.next


    def removeLast(self):

        if self.head == None :
            print("Nothing to remove")
            return
        
        temp = self.head
        while temp.next :
            prev = temp
            temp = temp.next

        prev.next = None
        return f'{temp.val} is removed from Last'
            

    def find(self, val):
        
        temp = self.head
        i = 1
        while temp :
            if temp.val == val :
                return(i)
            i += 1
            temp = temp.next


    def size(self):
        s = 0 
        temp = self.head

        while temp :
            s += 1
            temp = temp.next
        return s


    def displayLL(self):
        temp = self.head
        while temp :
            if not temp.next :
                print(temp.val)
            else :
                print(temp.val,end=" -> ") 
            temp = temp.next


if __name__ == '__main__':

    l = LinkedList()
    l.insertFirst(17)
    l.insertFirst(18)
    l.insertFirst(19)
    l.insertFirst(13)
    l.insertFirst(15)
    print(f'The element you were trying to find is at postion "{l.find(17)}"')
    l.insertFirst(12)
    l.insertMiddle(7,3)
    l.insertLast(1999)
    l.displayLL()
    print(l.removeFirst())
    print(l.removeLast())
    print(l.removeMiddle(5))

    l.displayLL()