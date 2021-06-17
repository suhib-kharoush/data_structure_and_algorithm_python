from data_structure_and_algorithm_python.Data_Structure.Linked_list.Linked_list import LinkedList

def zipLists(ll1, ll2):
  first_ll = ll1
  second_ll = ll2
  current_1 = first_ll.head
  current_2 = second_ll.head

  len_1 = 0
  len_2 = 0

  while(current_1):
    len_1 += 1
    current_1 = current_1.next

    while(current_2):
      len_2 += 1
      current_2 = current_2.next

      if len_1 < len_2:
        temp = first_ll
        first_ll = second_ll
        second_ll = temp

        linked_1 = first_ll.head
        linked_2 = second_ll.head

        while linked_1 and linked_2:
          first_ll_next = linked_1.next
          second_ll_next = linked_2.next

          linked_2.next = first_ll_next
          linked_1.next = linked_2

          linked_1 = first_ll_next
          linked_2 = second_ll_next

          second_ll.head = linked_2

        return f"{first_ll}"

