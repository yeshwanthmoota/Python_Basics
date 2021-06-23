# In python singly linked list is a header linked list.
class Node():
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
class Linked_list():

    def __init__(self):
        self.head = None
    
    def create_linked_list(self):
        self.head = None # creating a fresh linked list
        x = int(input("Enter how many elements you want to enter: "))
        # adding the first element
        for i in range(x):
            data = input("Enter the {} th element: ".format(i+1))
            self.insert_at_end(data)

    def insert_at_beg(self, data): # Here self is head
        node = Node(data, self.head)
        # now node.next points to what head was previously pointing to
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data, None)
            self.head = node
        else:
            ptr = Linked_list()
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next # do nothing
            # now ptr is pointing to the last node in the linked list
            node = Node(data, None) # created the node and making it point to the last
            ptr.next = node # linked the node to the present linked list
    def insert_at_pos(self, pos, data):
        i=1
        ptr = Linked_list()
        ptr = self.head # i=1 for ptr=self.head i.e. first element
        while i < pos-1:
            i += 1
            ptr = ptr.next
        # now i is at 'pos-1' position
        node = Node(data, ptr.next)
        ptr.next = node

    def display_list(self):
        if(self.head is None):
            print("Linked list is Empty")
        else:
            ptr = Linked_list()
            ptr = self.head # gave ptr the address of the head
            while ptr is not None:
                print(ptr.data)
                ptr = ptr.next

    def __len__(self):
        return self.len_linked_list()

    def len_linked_list(self):
        if(self.head is None):
            return 0
        else:
            count=0
            ptr = Linked_list()
            ptr = self.head
            while ptr is not None:
                count+=1
                ptr = ptr.next
            return count
    def search_element(self, data):
        if(self.head is None):
            print("Linked list is empty")
        else:
            ptr = Linked_list()
            ptr = self.head # gave ptr the address of the head
            i=0
            while ptr is not None:
                if(ptr.data == data):
                    print(f"The element is present in the linked list at position: {i+1}")
                    return i
                else:
                    i+=1
                    ptr = ptr.next
    def delete_element(self, data):
        if(self.head is None):
            print("Linked list is empty")
        else:
            x = self.search_element(data)
            print("deleting the element.........")
            self.delete_at_pos(x)
            print("deleted the element")
    def delete_at_pos(self, pos): # This will handle deletion at end, beginning, at 'pos' position also 
        if(pos == 0): # deleting the first element
            self.head = self.head.next
        else:
            ptr = Linked_list()
            ptr = self.head
            i = 0
            while i < pos-1:
                ptr = ptr.next
                i += 1
            # ptr is at pos-1 position
            ptr.next = ptr.next.next # Hence deleted the element.


list1 = Linked_list()

list1.insert_at_beg(245)
list1.insert_at_beg(352.67)
list1.insert_at_beg(112)
list1.insert_at_end("Hello")
list1.insert_at_beg("Monkey")
list1.insert_at_end(789)

list1.display_list()

list1.delete_element(352.67)
list1.insert_at_pos(pos = 3, data= 433.234)
list1.display_list()
# print("length of linked list is:", list1.len_linked_list())
print("length of linked list is:", len(list1))


# list1.create_linked_list() # creation of a fresh linked list
# list1.display_list()