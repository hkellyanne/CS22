__author__ = 'Kelly'


# if you set the debug variable below to True, it will dump your deque out in detail after each test before it tests
# with asserts

debug = False




class Node:

    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

# these are the defs you need for deque 

class Deque:

    def __init__(self): # construct a empty deque to start
        self.front = None
        self.rear = None

    def isEmpty(self):
        if (self.front == None) and (self.rear == None):
            return True
        else:
            return False



    def addFront(self,data):
        current = Node(data)
        if self.isEmpty() is False:
            current.next = self.front
            self.front.prev = current
        else:
            self.rear = current
        self.front = current

        return data

    def addRear(self,data):
        current = Node(data)
        if self.isEmpty() is False:
            current.prev = self.rear
            self.rear.next = current
        else:
            self.front = current
        self.rear = current

        return data


    def removeFront(self):
        current = self.front
        temp = self.front.data
        self.front = self.front.next
        self.front.prev = None
        if self.front.next is None:
            self.front = None

        return temp

        # removes front node and returns data reference
        # return None if empty deque

    def removeRear(self):
        current = self.rear
        temp = self.rear.data
        self.rear = self.rear.prev
        self.rear.next = None
        if self.rear.prev == None:
            self.rear = None

        return temp




        # removes rear node and returns data reference
        # return None if empty deque

    def pop(self,index):
        head = self.front
        end = self.rear
        self.pop(index)
        if index < 0:


        # remove noded indexed: index indicated by index 0,1,2 count from front to rear
        # index -1,-2,-3 counts from rear toward front
        # return None if list is empty before pop

        pass


    def size(self):
        count = 0
        if self.front != None:
            count = 1
            current = self.front
            while current.next != None:
                count += 1
                current = current.next
        return count


    def __str__(self): # print deque
        node = self.front
        s = ""
        while node is not None:
            s += str(node.data) + ", "
            node = node.next
        return "[ " + s[0:-2] + " ]"

    _nodes = {} # dictinary to map node id to n1, n2, n2 to make reading dump easier
    _index = 1 # used to keep track of first n that is not used in node names

    def peekFront(self): # return front node data reference or None
        if self.front == None: return None
        return self.front.data

    def peekRear(self): # return rear node data reference or None
        if self.rear == None: return None
        return self.rear.data

    def dump(self): 

        def addr(x):
            if x is None:
                return "None"
            else:
                if id(x) in self._nodes:
                    return self._nodes[id(x)]
                else:
                    self._nodes[id(x)] = "n%d"%(self._index)
                    self._index += 1
                    return self._nodes[id(x)]

        print ("  ","-"*20," DUMP of Deque ","-"*20)
        print ("    self.front: " , addr(self.front))
        node = self.front

        while node is not None:
            print ("\n     Node: ",addr(node))
            print ("         data: ",node.data)
            print ("         next: ",addr(node.next))
            print ("         prev: ",addr(node.prev))
            node = node.next
        print( "\n    self.rear: ", addr(self.rear) )
        print( "  ", "-"*50)

    def integrity_check(self):
        if self.front == None:
            assert self.rear is None, "rear is not None for empty deque"
        else:
            forward = []
            node = self.front
            while node is not None:
                forward.append(node)
                node = node.next
            node = self.rear

            node = self.rear
            while node is not None:
                assert forward.pop() == node,\
                "prev for node does not match \n" +\
                str(id( forward[ len(forward)-1 ])) + " <=> "+ str(id(node)) +\
                "for node number " + str(len(forward))
                node = node.prev


def main():

    dq = Deque()
    print("new Deque(), and the size is ", dq.size())
    print("dq after: ", dq)
    if debug: dq.dump()
    dq.integrity_check()

    dq.addFront(11)
    print("dq.addFront(11), dq after: ", dq) # 0
    if debug: dq.dump() 
    assert dq.size() == 1, "size should now be 1"
    assert dq.peekFront() == 11, "front node data should be 11"
    assert dq.isEmpty() == False , "isEmpty should return False"
    dq.integrity_check()

    dq.addFront(22)
    print("dq.addFront(22), dq after: ", dq) # 0
    if debug: dq.dump() 
    assert dq.size() == 2, "size should now be 2"
    assert dq.peekFront() == 22, "front node data should be 22"
    assert dq.peekRear() == 11, "rear node data should be 11"
    dq.integrity_check()

    dq.addFront(55)
    print("dq.addFront(55), dq after: ", dq) # 0
    if debug: dq.dump() 
    assert dq.size() == 3, "size should now be 3"
    assert dq.peekFront() == 55, "font node data should be 22"
    dq.integrity_check()

    data = dq.removeFront()
    print("dq.removeFront(), dq after: ", dq)
    if debug: dq.dump()
    assert data == 55, "removeFront() should return 55"
    assert dq.peekFront() == 22, "front node data should now be 22"
    assert dq.size() == 2, "size should now be 2"
    dq.integrity_check()

    dq.addRear(9)
    print("dq.addRear(9), dq after: ", dq)
    if debug: dq.dump()
    assert dq.size() == 3, "size should now be 3"
    assert dq.peekRear() == 9, "front node data should now be 9"
    dq.integrity_check()

    dq.addRear(1)
    print("dq.addRear(1), dq after: ", dq)
    if debug: dq.dump() 
    assert dq.size() == 4, "size should now be 4"
    dq.integrity_check()

    dq.addRear(99)
    print("dq.addRear(1), dq after: ", dq)
    if debug: dq.dump() 
    assert dq.size() == 5, "size should now be 5"
    dq.integrity_check()

    data = dq.removeRear()
    print("dq.removeRear(), dq after: ", dq)
    if debug: dq.dump() 
    assert data == 99, "removeRear() should return 1"
    assert dq.peekRear() == 1, "Rear node data should now be 22"
    assert dq.size() == 4, "size should now be 4"
    dq.integrity_check()

    print("-------\nNOW EXTRA CREDIT TESTS:\n")

    n = dq.pop(1)
    print("dq.pop(1), dq after: ", dq)
    if debug: dq.dump()
    print("  returned: ",n)
    if debug: dq.dump() 
    assert n == 11, "pop(1) should have returned 9 "
    assert dq.size() == 3, "size should now be 3"
    dq.integrity_check()

    n = dq.pop(-1)
    print("dq.pop(-1), dq after: ", dq)
    print("  returned: ",n)
    if debug: dq.dump()
    assert n == 1, "pop(-1) should have returned 1 "
    assert dq.size() == 2, "size should now be 2"
    dq.integrity_check()

    n = dq.pop(0)
    print("dq.pop(0), dq after: ", dq)
    print("  returned: ",n)
    if debug: dq.dump()
    assert n == 22, "pop(0) should have returned 22 "
    assert dq.size() == 1, "size should now be 1"
    dq.integrity_check()

    n = dq.pop(-1)
    print("dq.pop(-1), dq after: ", dq)
    print("  returned: ",n)
    if debug: dq.dump() 
    assert n == 9, "pop(-1) should have returned 9 "
    assert dq.size() == 0, "size should now be 0"
    assert dq.isEmpty() == True , "isEmpty should return True"
    dq.integrity_check()

main()

