from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        #self.buffer ={} unnecessary

    def append(self, item):
        #key = self.storage.length
        if self.capacity== self.storage.length:
            self.storage.remove_from_head() #remove oldest
            self.storage.add_to_head(item)
            #key = capacity - 1 #unnecessary now
            #self.buffer[key] = value #overwrite the old # actually this is just redo'ing array functionality but worse
        elif self.capacity > self.storage.length:
            self.storage.add_to_tail(item) #this will add it to the head too if no head
            #self.buffer[key] = value
        #self.length += 1 unnecessary


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        self.current = self.storage.head
        i = 0
        for i in range(self.storage.length):
            if self.current:
                list_buffer_contents.append(self.current.value)
                self.current = self.current.next
            else:
                continue
            i += 1


        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
