from data_structure_and_algorithm_python.Challenges.queue_with_stacks.queue_with_stacks import PseudoQueue, Stack

queue = PseudoQueue()

def test_enqueue():
    queue.enqueue('first level')
    queue.enqueue('second level')
    queue.enqueue('third level')
    queue.enqueue('fourth level')
    assert queue.__str__() == "first level\nsecond level\nthird level\nfourth level"
    queue2 = PseudoQueue()
    queue2.enqueue('first level')
    assert queue2.__str__() == 'first level'

def test_dequeue():
    assert queue.dequeue() == 'first level'
    assert queue.dequeue() == 'second level'
    assert queue.__str__() == 'third level\nfourth level'