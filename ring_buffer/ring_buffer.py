from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        self.oldest = None
        self.new_oldest = None
        self.newest = None
        #self.buffer ={} not allowed


    def append(self, item):
        #key = self.storage.length


        if self.capacity== self.storage.length:
            if self.oldest == self.storage.head:
                self.storage.remove_from_head() #remove oldest
                self.storage.add_to_head(item)
                self.oldest = self.oldest.next
            elif self.oldest == self.storage.tail:
                self.storage.remove_from_tail() #remove oldest
                self.storage.add_to_tail(item)
                self.oldest = self.storage.head
            else:
                self.storage.add_to_tail(item)
                self.storage.move_to_end(self.storage.tail.prev)
                self.new_oldest = self.oldest.next
                self.storage.move_to_end(self.oldest)
                self.storage.remove_from_tail()
                self.storage.head.insert_before(self.storage.tail.prev.value)
                self.oldest = self.new_oldest
                print(self.new_oldest.value)
            # self.oldest.delete()
            # self.oldest.insert_before(item)

            #self.storage.move_to_front(self.oldest)
            # self.oldest = self.oldest.nexts
            #self.storage.remove_from_head()

            #key = capacity - 1 #unnecessary now
            #self.buffer[key] = value #overwrite the old # actually this is just redo'ing array functionality but worse
        elif self.capacity > self.storage.length:
            self.storage.add_to_tail(item) #this will add it to the head too if no head
            #self.buffer[key] = value
            if self.storage.length == 1:
                self.oldest = self.storage.head
                print(self.oldest)
        #self.length += 1 unnecessary

#----------------------------------------------------------------------------------------------------------

    # def append(self, item):

    #     if self.capacity== self.storage.length:
    #         if self.oldest == self.storage.head:
    #             #self.oldest.insert_after(item)            
    #             self.new_oldest = self.oldest.next
    #             self.storage.add_to_head(item) 
    #             self.storage.move_to_front(self.oldest)           
    #             self.storage.remove_from_head() #remove oldest
    #             self.oldest = self.new_oldest   
    #             self.newest = self.storage.tail
    #         elif self.newest ==self.storage.tail: 
    #             self.newest.insert_before(item)            
    #             self.new_oldest = self.oldest.next
    #             self.storage.add_to_head(item) 
    #             self.storage.move_to_front(self.oldest)           
    #             self.storage.remove_from_head() #remove oldest
    #             self.oldest = self.new_oldest
    #             self.newest = self.newest.prev
    #         else:  
    #             self.newest.insert_before(item)            
    #             self.new_oldest = self.oldest.next
    #             self.storage.add_to_head(item) 
    #             self.storage.move_to_front(self.oldest)           
    #             self.storage.remove_from_head() #remove oldest
    #             self.oldest = self.new_oldest
    #             self.newest = self.newest.prev

    #         # self.oldest.delete()
    #         # self.oldest.insert_before(item)


    #         # self.oldest = self.oldest.next
    #         #self.storage.remove_from_head()

    #     elif self.capacity > self.storage.length:
    #         self.storage.add_to_tail(item) #this will add it to the head too if no head

    #         if self.storage.length == 1:
    #             self.oldest = self.storage.head
    #             print(self.oldest)






#SUBMITTED
    # def append(self, item):
    #     #key = self.storage.length


    #     if self.capacity== self.storage.length:
    #         self.storage.remove_from_head() #remove oldest
    #         self.storage.add_to_head(item)
            
    #         # self.oldest.delete()
    #         # self.oldest.insert_before(item)

    #         #self.storage.move_to_front(self.oldest)
    #         # self.oldest = self.oldest.next
    #         #self.storage.remove_from_head()

    #         #key = capacity - 1 #unnecessary now
    #         #self.buffer[key] = value #overwrite the old # actually this is just redo'ing array functionality but worse
    #     elif self.capacity > self.storage.length:
    #         self.storage.add_to_tail(item) #this will add it to the head too if no head
    #         #self.buffer[key] = value
    #         if self.storage.length == 1:
    #             self.oldest = self.storage.head
    #             print(self.oldest)
    #     #self.length += 1 unnecessary


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
