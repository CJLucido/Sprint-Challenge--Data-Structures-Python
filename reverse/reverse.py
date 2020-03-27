class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None

    def add_to_head(self, value):
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False
        # get a reference to the node we're currently at; update this as we
        # traverse the list
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our
            # target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def reverse_list(self, node, prev):
        # You must use recursion for this solution
        if not node:
            return
        else:
            next_node_to_switch_places = node.get_next()
            print(next_node_to_switch_places.value)
            if not next_node_to_switch_places:
                return
            else:
                new_prev = next_node_to_switch_places.get_next()

            if prev == None:
                node.set_next(None)
                
            else:
                node.set_next(prev)
            

            if not new_prev:
                return
            else:
                self.reverse_list(next_node_to_switch_places, new_prev)      
            


#Plan--------------------------------------------------------------

# capture the next
# next_node_to_switch_places = head.next
# head.prev = head.next
# head.next = head.prev (or none) #if/conditional
# recursive(next_node_to_switch_places)

# runthrough:
# next_node_to_switch_places = 2
# head.prev = 2
# head.next = none
# recursive(next_node_to_switch_places/2)
# 2 1 none 3 none
# next_node_to_switch_places = 3
# head.prev = 3
# head.next = 1
# recursive(next_node_to_switch_places/3)
# 3 none 2 1 none
# next_node_to_switch_places = none #if/conditional, once this happens don't call the recursive function
# head.prev = none (conditional?)
# head.next = 2
# if next_node_to_switch_places == None:
# 	return
# else:
# 	recursive(next_node_to_switch_places/3)
