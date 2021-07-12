- a) In the first pass we evalute if the length of the list is greater than 1, after that we assigned every half of the list to the left and right variables and we kept calling the function and divide the left and right until every list will have 1 element.
- [20,18,12,8,5,-2] -> [20,18,12] [8,5,-2] -> [20,18][12][8,5][-2]->[20][18][12]...[8][5][-2]

- b) In the second pass that we merged the lift and right side of the list in sorted way.
- [20] [12]
- [18,20] [5,8]
- [12,18,20] [-2,5,8]
#### [-2,5,8,12,18,20]