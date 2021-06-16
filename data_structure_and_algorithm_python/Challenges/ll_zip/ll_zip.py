from data_structure_and_algorithm_python.Data_Structure.Linked_list.Linked_list import LinkedList

def zipLists(list_one, list_two):
    if not list_one:
        return list_two
    elif not list_two:
        return list_one
    zip_list = LinkedList()
    current = list_one
    current = current.head
    current_2 = list_two.head

    while current or current_2:
        if current:
            zip_list.append(current.data)
            current = current.next_node
        return zip_list
            
