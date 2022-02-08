def removeDuplicates(llist):
    # Write your code here
    node = llist
    
    while node.next != None:
        if node.data == node.next.data:
            node.next = node.next.next
            continue
        node = node.next
  
    return llist
