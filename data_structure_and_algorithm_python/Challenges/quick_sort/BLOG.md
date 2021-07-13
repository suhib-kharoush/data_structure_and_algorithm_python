# Tracing
1. consider the pivot as a last element, then divide the list.
2. In partition, the list is broken into 2 sub lists and all of the elements are smaller than the pivot will be on the left side of the pivot and the bigger elements will be on the right.
3. The pivot will be on the last position.
4. sub elements on the right and left side don't require to be sorted.
5. Then we recursively pick the left and right sub-lists, and we perform partitioning on each of them by choosing a pivot in the sub-lists and the steps are repeated for the same.

![](quick_sort_blog.PNG)