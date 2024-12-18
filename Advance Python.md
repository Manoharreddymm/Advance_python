`                            `**Advance Python**

**Testing and debugging**

Testing:

`	`The processes of evaluating the python code to ensure its behaviour as expected.

There are mainly 2 testing:

1. Manual testing- the tester executes the code without any tools. 
   1. Human interaction
   1. Expolatory  testing 
   1. Ad-Hoc testing
   1. Usability testing
   1. Functionality testing
1. Automatic testing – tester uses some tools like unittest,selium,pytest.
   1. Unit testing
   1. Integrated testing
   1. Functionality testing
   1. Regression testing 
   1. Automatic testing

Debugging:

`	`Debugging is used to find the errors in the code after the execution and then resolve it and re run the code.

Steps in debugging:

1. Identify the bug
1. Reproduce the bug
1. Analyse the bug
1. Fix the bug
1. Test the bug

Types of errors:

1. Syntax error 
1. Logical error
1. Name error
1. Type error
1. Value error


**Decorators:**

`	`The decorators are used to décor or enhance the functionality in a flexible and reusable way.

Decorators are used to extend the behaviour of the function without changing its structure permanently.

They are the way of add one function with another function that adds the additional information  before or after the execution.

@function\_name

By using this we can add another function the main function. In this decorators the function can be stored in variable, passing function as argument and returning functions from another functions.

**Functional programming:**
**
`	`Functional programming is programming paradigm (organize the code around the object that combine the data and object) that treats computation as evaluation of mathematical functions and avoid changing state and mutable data.

**Pure function:**

`	`It always produce the same output for the same arguments. It does not change or modify the input arguments.

**Recursion:**

`	`Recursion is the process where the function call itself directly or indirectly.

**Lambda:**

`	`The use of lambda function when requires the name less function stored for shorter period of time.

It will take any number of arguments and necessary function.

X=lambda a : a\*\*a

**Filter:**
**
`	`The filter function fits the sequence with the help of function.

**Map:**
**
`	`map the entire functionality to each and every element of the sequence.

**Reduce:**
**
`	`the entire function is applied to all the values of the sequence and reduce to single value.

`                             `DSA

**Sorting:** The sorting is used for arrange the data in a ascending or descending order.

Selection sort: 

`	`In the selection sort the smallest value is sorted first.

Working of the selection sort is we are taking a unsorted list and firstly we are taking a min value at the staring the index and starts iteration. We are going to compare the min index value with others if min is greater than other value we are swapping the values present in the min and present iterated index. After the first iteration the smallest value is sorted first and continuous the same process for entire list.



**Bubble sort:**

`	`In the bubble sort the largest value is going to sorted first.

Working of bubble sort is so simple we are checking 2 adjacent values to sort the list. We are going to compare the two values if the arr[0] is greater than arr[1] the we are swapping the values present in the specific index. After the first iteration the largest value is sorted first and continuous the process until the list is sorted.

**Insertion sort:**

`	`In insertion sort we are sorting the list going to sort based on the key value.

Working of the insertion  sort is very simple we are assuming the first element in the list as sorted and other elements are unsorted. We are dividing the list in sorted and unsorted list where the index 0 is assume as sorted and comparing with right side value if the value is greater than the key value we are not going to swap the value if the value is smaller than the left value until the index0. Once the left most is element is sorted then shifting the key value to the index1 and continuous process until the list is sorted.

**Quick sort:**
**
`	`We are have draw backs of using the other sorting algorithms because it takes more time for sorting so we are taking the quick sort for fast sorting.

`	`Working of the quick sort: we are randomly picking a pivot value from the list. In the quick sort one element is sorted at its own position. After picking the pivot value we are taking 2 variables like start and end start the iteration from left most and check if the value is less than pivot value if less move right side until the pivot value is greater than the present index then stop and starts checking from backwards if the index is greater than the pivot value it moves left. If the value is less than the pivot then stop and we are going to swap the start and end values. If the start index cross the end index then we are swapping the pivot and end values. Then this process is repeating until the list got sorted.

**Merge sort:**
**
`	`The merge sort is dived and conquer where the list is  diving the list and sorting.

Working of merge sort: In the merge sort we are dividing the list into 2 equal parts and then sorting the divided list and combining them. Firstly we are dividing the list into 2 equal parts and the we are dividing the divided list and swap the elements into order and merge.

**Searching:**
**
`	`The searching is used to find a specific value in the list.

**Linear search:**
**
`	`The linear search is used to find the value in a unsorted list where we are finding the search value from starting of the index to end index value. It search from staring of the list using the search variable if search == index[i] the it will return the index of the value.

**Binary search:**   

`	`The binary is used to find a variable if the list is sorted. If the list is not sorted then first sort the list and then apply binary search. First the list divided into 2 equal parts checks if the search value is greater than or less than or equal to the mid value. By checking search value with the mid value it will gets an idea weather it will left or right. Once the search value is found then it will return its index value.

**LINKED LIST**
**
`	`Linked list is a linear data structure contains a node. A node contain data and next node address. The list is used to overcome the drawbacks of the list and array. The list is also a dynamic allocation only while creating a list it dynamically generates a place in the memory in the list with some fixed space when we are appending more than the size of the list it will reassign the new block for entire list so it will take more time for copying the data to overcome this problem we are using the linked list.

Types of linked list:

1. Singly linked list
1. Doubly linked list
1. Circular linked list

Singly linked list:

`	`In the singly linked list we can only traverse in one direction only. We can do operations like adding a element, removing, searching etc.,

For insertion and deletion at starting of the list takes O(1).

For inserting, searching, deletion at last or random can take O(n). 

Doubly liked list:

`	`In the singly linked list we have no link to the backwards to overcome this we are storing  the  previous node address in the present node so that we can traverse backwards also in the doubly linked list.

Circular linked list:

`	`In the circular linked list we are connection the node with the head node so we are having the loop in the linked list it is easy to traverse in the list.

**Stack:**
**
`	`The stack is a linear data structure stores the items in the last in first out manner. The adding and removing the items is takes place at one end.

It takes O(1) for adding and removing the elements.

Pushing- inserting the element into the stack.

Pop-  removing the item into the stack.

Functions in the stack:

1\.push()

2\.pop()

3\.top() or peek()-returns the top value

4\.size()

5\.Empty()

Implementations in the stack:

`	`1.list

`	`2.collection.deque

`	`3/queue.LifoQueue

`	`4.linked list

**Queue:**
**
`	`the queue is a linear data structure that stores the elements in the first in first out. The last recently added item is removed first.

Implementation of queue:

`	`1.list

`	`2.deque

`	`3.LifiQueue

**Trees:**
**
`	`The tree is a non linear data structure it contains a nodes. The tree structure has a tree like structure having root node and to that node a child node is connected to it.

It contains a main parent root by connection to the root there are some child nodes connected to it. The root node is the starting node and the leaf node node refers to the last node .

Implementation of trees:

1\.linked list

2\.arrays

Tree traversal techniques:

1\.in-order traversal.

2\.pre\_order traversal.

3\.post-order traversal.

**Binary search tree:**
**
`	`In the binary search tree the items in the tree is going to be ordered where as the root node left contain less value and right contains large value.

The searching is done easly by the binary search tree.

Root.left > key

Root.right< key.

**Graphs:**
**
`	`The graph is a non-linear data structure containg vertices and edges. The graph is a group of vertices and edges are used to connect the vertices.

A graph is seen as a cycle.

G(V,E)

The graphs may be uni-directional or bi-directional.

Implementations of graphs:

1\.linked list

2\.list

Searching in Graphs:

1\.Breadth first search

2\.Depth first search

BFS: In the BFS we can go to any nodes that are connected to the node.

DFS: We cannot go the every node that are connected to the node because first we need to go through one node and if it contains n no of nodes choose one node and the after completing that node we are coming back to the main node and them go to other nodes that are connected to it.

**Concurrency and parallelism**
**
`	`To increase the speed of a process or operation we use the concurrency and parallelism. By executing the multiple tasks in parallel between multiple tasks.

Parallelism- allows several tasks to run side by side on independent partition resource.

`		`Ex- cores in the cpu

Concurrency- the ability of different parts of unit of a program or algorithm to be execute out 		of order without affecting the outcome.

Allows multiple jobs to take accessing the same shared resource and main goal concurrency to prevent tasks of blocking each other by switching among when one is forced to wait on external resource.




**


**Iterators:**
**
`	`Iterator is a object which contain countable number of values used to iterate over iterable objects like list, set, tuples etc,. they are implemented using classes, here  local variablesis not required for iteration. It follows lazy evoluation where evaluation of expression hold and store memory.

The memory is saved when we are using large data because of the lazy evaluation.

- Iter()- used to create iterator
- Next()-used to call the next value in the iterator 

**Generators:**
**
`	`The generator uses keyword yield. It is implemented using functions it will not disturb the flow of the functions and return the values using the  yield . generators are also follows the lazy evaluation.

- Every generator is an iterator.

**Meta class:**
**
`	`The class that defines the behaviour of other classes and is used to create and manipulate class at run time.  Metaclasses allow for code not only to manipulate data, but to manipulate classes. Often this change happens when an object of the class is instantiated. Using metaclasses also helps to abstract our code, making it more readable and helping to reduce the amount of code written by avoiding repetition in code.**	 	 


**






