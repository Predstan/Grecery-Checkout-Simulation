# Implementation of Queue ADT Using LinkedList
class queue:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.size = 0

    # Determines if Queue is Empty
    def isEmpty(self):
        return self.head is None

    # Returns the Length of of items in the queue
    def __len__(self):
        return self.size

    # Adds and enqueue an item
    def enqueue(self, item):
        newNode = queueNode( item )
        if self.head is None:
            self.head = newNode
            self.tail = self.head

        else:
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1

    # Return and Remove an Item from the Queue Using FIFO
    # Fist in Fist Out ( FIFO )
    def dequeue(self):
        assert not self.isEmpty(), \
            " Queue is Empty"
        if self.head == self.tail:
            self.tail = None
        item = self.head.data
        self.head = self.head.next
        self.size -= 1
        return item
    
# Storage Class for Queue Node and Item
class queueNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None




