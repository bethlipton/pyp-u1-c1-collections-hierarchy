class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        
s = Node('X', Node('Y', Node('Z')))

print (s.value)

#identifying the current node
current = s

#printing all nodes in the sequence
while current is not None:
    print(current.value)
    current = current.next
#using .next to iterate through the sequence
print("--------")
print(s.next.next.value)