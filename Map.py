# __author__ = 'Kelly'



def again(i):
    print("+")
    if i < 0:
        return 0
    return again(i-3) * 4 + 2

again(10)



class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [[list() for x in range(self.size)]] * self.size
        self.data = [None] * self.size

    def put(self,key,data):
      hashvalue = self.hashfunction(key,len(self.slots))

      if self.slots[hashvalue] == None:
        self.slots[hashvalue] = key
        self.data[hashvalue] = data
      else:
        if self.slots[hashvalue] == key:
          list.append(self.data[hashvalue])  #replace
        else:
          nextslot = self.hashfunction(0)
          start = nextslot
          while self.slots[nextslot] != None and self.slots[nextslot] != key:
            nextslot = self.rehash(nextslot,len(self.slots))
            if nextslot == start: # error, we have loop all the way round
                raise RuntimeError("Map is full")

          if self.slots[nextslot] == None:
            self.slots[nextslot]=key
            self.data[nextslot]=data
          else:
            self.data[list.append()] = data #replace

    def hashfunction(self,key,size):
         return key%size

    def rehash(self,oldhash,size):
        return (oldhash+1)%size

    def get(self,key):
      startslot = self.hashfunction(key,len(self.slots))

      data = None
      stop = False
      found = False
      position = startslot
      while self.slots[position] != None and  \
                            not found and not stop:
         if self.slots[position] == key:
            found = True
            data = self.data[position]
         else:
            position=self.rehash(position,len(self.slots))
            if position == startslot:
                stop = True
      return data

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)

H = HashTable()
H[54]="cat"
H[26]="dog"
H[93]="lion"
H[17]="tiger"
H[77]="bird"
H[31]="cow"
H[44]="goat"
H[55]="pig"
H[20]="chicken"
print(H.slots)
print(H.data)

print(H[20])
 
  print(H[17])
  H[20]='duck'
  print(H[20])
  print(H[99])

 ## TEST FOR HashTable
 h = HashTable() # create new hash table

 nums = [1, 3, 5, 50, 1000] # some keys
 nums = nums + [ len(h.slots)*i for i in range(20)] # some keys that have same hash
 vals = vals = [ chr(x) for x in range(ord('A'),ord('Z')) ] # list of single letters from A to Z

 # add key/values
 for i in range(len(nums)):
     # print("adding (%d, %s)"%(nums[i],vals[i]),end=" ")
     h[nums[i]] = vals[i]

 for i in range(len(nums)):
     key = nums[i]
     value = vals[i]
     gotValue = h[key]
     assert gotValue == value,"expected key: %d to lookup value: %s but got value %s instead " % (key, value, gotValue)

 print("\nAll TESTS PASSED")
