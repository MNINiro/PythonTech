def main():

    class Node:
        def __init__(self, data):
            self.data = data
            self.next_node = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def AppendNode(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node

        if self.tail != None:
            self.tail.next = new_node

        self.tail = new_node

    def PrintList( self ):
        node = self.head

        while node != None:
            print (node.data)
            node = node.next

    def PopNode( self, index ):
        prev = None
        node = self.head
        i = 0

        while (node != None ) and ( i < index ):
            prev = node
            node = node.next
            i += 1

        if prev == None:
            self.head = node.next
        else:
            prev.next = node.next

list = LinkedList()
list.AppendNode(1)
list.AppendNode(2)
list.AppendNode(3)
list.AppendNode(4)
list.PopNode(0)
list.PrintList( )
