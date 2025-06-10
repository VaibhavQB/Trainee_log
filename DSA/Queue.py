# QUEUE Implementation Using Class

class Queue:
    def __init__(self, size):
        self.queue = []
        self.size = size

    def queuelen(self):
        return len(self.queue)

    def isFull(self):
        return self.queuelen() == self.size

    def isEmpty(self):
        return self.queuelen() == 0

    def enqueue(self, val):
        if self.isFull():
            print("Queue is FULL! Can not Enqueue another item")
        else:
            self.queue.append(val) 

    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty! Can not Dequeue item")
        else :
            return self.queue.pop(0)

    def last(self):
        if self.isEmpty() :
            return "No Items in Queue"
        return self.queue[-1]
    
    def first(self):
        if self.isEmpty():
            return "No items in Queue"
        return self.queue[0]
    
    def __str__(self):
        return str(self.queue) if not self.isEmpty() else "Queue is Empty"


if __name__ == "__main__":
    
    q = Queue(7)
    q.enqueue(10)
    q.enqueue(1)
    q.enqueue(17)
    q.enqueue(91)
    q.enqueue(179)
    q.enqueue(99)
    q.enqueue(100)

    q.enqueue(1088)
    print(q.first())
    print(q.last())

    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()

    q.dequeue()
    q.dequeue()
    q.dequeue()

    print(q.first())
    print(q.last())