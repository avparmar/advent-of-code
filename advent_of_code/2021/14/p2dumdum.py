from collections import defaultdict

with open('inputs/p1/input.txt') as input:
  rows = [x for x in input.read().strip().split("\n")]
  input.close()

template = rows[0]

rules = {}

strptr = 0

for row in rows[2::]:
  if not row:
    continue
  a, b = row.split(' -> ')
  rules[a] = b

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None

nn = LinkedList()
nn.head = Node(template[0])

curr = nn.head
for char in template[1:]:
  nex = Node(char)
  curr.next = nex
  curr = nex

"""bla = nn.head  
while bla is not None:
  print(bla.data)
  bla = bla.next"""

bla = nn.head
"""stst = ""
while bla is not None:
  stst += bla.data
  bla = bla.next
print(stst)
print()"""

bla = nn.head
for i in range(14):
  bla = nn.head
  prev = None
  curr = None
  while bla is not None:
    #print(prev.data, bla.data)
    #if prev:
      #print(prev.data,bla.data)
    if prev is None:
      prev = bla
    else:
      cd = bla.data
      pd = prev.data
      tmp = pd + cd
      #print("prev:" + prev.data)
      #print("tmp:" + tmp)
      #print("bla:" + bla.data)
      if tmp in rules:
        newGuy = Node(rules[tmp])

        prev.next = newGuy
        newGuy.next = bla
        prev = bla
      else:
        prev = prev.next
    bla = bla.next

"""print()
bla = nn.head
stst = ""
while bla is not None:
  stst += bla.data
  bla = bla.next
print(stst)"""

cts = defaultdict(int)

bla = nn.head
while bla is not None:
  cts[bla.data] += 1
  bla = bla.next
#for char in newT:
  #cts[char] += 1

print(cts)

#3115 - 921