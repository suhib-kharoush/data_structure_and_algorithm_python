# Hashtable

- hash table or hash map is a data structure that implement as associative list abstract data type.It uses a hash function to compute an index.During lookup, the key is hashed and the resulting hash indicates where the corresponding value is sorted.


### Challenge:
- Implement a Hashtable with the following methods:

- - add: takes in both the key and value. This method should hash the key, and add the key and value pair to the table, handling collisions as needed.

- - hash: takes in an arbitrary key and returns an index in the collection.


- - get: takes in the key and returns the value from the table.

- - contains: takes in the key and returns a boolean, indicating if the key exists in the table already.


### Approach & Efficiency:
- Big O for both space and time is O(1) except the worst case O(n)