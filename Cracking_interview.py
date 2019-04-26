#implement linkedlist # remove duplicates from not sorted LinkedList
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None
        self.lastnode=None

    def append(self,value):
        if self.lastnode is None:
            self.head=Node(value)
            self.lastnode=self.head
        else:
            self.lastnode.next=Node(value)
            self.lastnode=self.lastnode.next

    def get_prev_node(self, ref_node):
        current=self.head
        while (current and current.next!=ref_node):
            current=current.next
        return current

    def remove(self, node):
        prev_node=self.get_prev_node(node)
        if prev_node is None:
            self.head=self.head.next
        else:
            prev_node.next=node.next

    def display(self):
        current=self.head
        while current:
            print(current.value, end='')
            current=current.next

def remove_duplicates(ll):
    current1=ll.head
    while current1:
        value=current1.value
        current2=current1.next
    while current2:
        if current2.value==value:
            ll.remove(current2)
            current2=current2.next
    current1=current1.next

#Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word
#or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters.
#The palindrome does not need to be limited to just dictionary words.
def perm_pal(s):
    lookup={}
    odd=0
    for char in s:

    if lookup.get(char)!=None:
    lookup[char]+=1
    else:
    lookup[char]=1
    for key in lookup.keys():
    if lookup[key]%2!=0:
    odd+=1
    if odd>1:
    return False
    else:
    return True
