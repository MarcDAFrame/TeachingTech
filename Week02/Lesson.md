# Week 2: Fundamentals of software development
## Outline


# Terminal
![terminal](<./res/terminal.jpeg>)
text based interface of your computer. Allows you to enter commands, manipulate files, execute programs, run code ... all via the command line (CLI) in a shell script (`bash` for Linux / OSX and `batch` for Windows).

# Bash


## Most important commands
```bash
# list items in directory (current direc◊tory)
ls
# list items in directory
ls /path/to/directory 
# list with more info (permissions, creator, size, last modified)
l
# change directory (absolute path)
cd /path/to/directory
# change directory (relative path cwd)
cd ./relative/to/current/working/directory
# print current working directory
pwd
# copy file
cp FILENAME1 FILENAME2
# copy folder
cp -r FOLDER1 FOLDER2
# remove file
rm FILENAME
# remove folder
rm -rf folder
# move / rename file
mv OLDFILENAME NEWFILENAME
# move folders
mv ./PATH/FOLDER ./PATH/NEWFOLDER
# make folder
mkdir FOLDERNAME
# make file
touch FILENAME
# edit file (can also create files)
nano FILENAME
# view contents of a file
cat FILENAME
# view current resource utilization
htop
# view processes
ps
# kill a process (PROCESS_ID or PID found with 'top' or 'ps' command)
kill PROCESS_ID
# ping (used to check connectivity)
ping google.com
ping 8.8.8.8
```


# Data Structures
![data structure](<./res/datastructure.png>)
## Array
![linked list](<./res/array.png>)

```python
# 1D array
a_1d = [3,2]
a_1d[0] # 3

# 2D Array
a_2d = [[1,0,1], [3,4,1]]
a_2d[0][0] # 1

# 3D Array
a_3d = [
    [ [1,7,9], [5,9,3], [7,9,9] ],
    [ [1,1,1], [1,1,1], [1,1,1] ],
]
a_3d[0][0][0] # 1
a_3d[0][1][3] # 3
```

## Linked List
![linked list](<./res/linkedlist.png>)
- represents
    - anything an array does, but worse

## Stack
![stack](<./res/stack.webp>)
- represents
    - undo / redo buttons (`ctrl + z` ... )
    - evaluating mathmatical expressions (`"1 + 1 = 2" -> [1, "+", 1, "=", 2] -> pop'd and evaluated`)
- last in first out (LIFO)

## Queue
![queue](<./res/queue.webp>)
- represents
    - customers in line
- first in first out (FIFO)

## Hashtable, hashset
![hash table](<./res/hashtable.png>)
- represents
    - dictionaries
    - sets

```python
# hashtable (aka dictionary)
hashtable = {
    "a" : 123,
    "b" : 456,
}

hashtable["a"] # 123
hashtable["b"] # 456
hashtable["c"] # KeyError: 'c'

# set
hashset = set([1,2,3,1,2,3])
print(hashset) # {1,2,3}
```

## Tree
- represents
    - XML / HTML
    - binary search trees
    - decision trees (i.e. pick your own adventure games)

### Binary Tree
![ordered bt](<./res/orderedbt.png>)
- tree with additional rules
- max two children
- can be **ordered**
    - i.e. left, smaller than right
    - makes searching very fast (i.e. divide and conquor, binary search)
    - can be very expensive to add / remove from tree as it may require complete restructuring of the tree

## Graph
![graph](<./res/graph.png>)
- represents
    - transit networks
    - relationships between people
- types
    - directed
    - undirected
    - weighted




# Algorithms
![sort](<./res/sort.gif>)
a specific procedure for solving a well-defined computational problem.

Not going to go into too much detail about these because
1. your education will teach you
2. you probably won't have to implement one yourself

But generally, an algorithm generally breaks down to an application of a datastructure

Here's some examples of Algorithms and Data Structures used to implement them
- Binary Search : Binary Tree
- Shortest Path Algorithms : Graph
- CPU Scheduling : Queue





# Big O Notation
![big o](<./res/bigo.png>)
Big O notation is a measure of analysing theoretical efficiency of an algorithm.

Essentially, Big O gives you an idea of how the execution time will change as the input set size increases.

Some algorithms will run as fast regardless of the size of the input set, some will increase faster.

## O(1)
It will run in one operation regardless of input size.

### Examples
- hashtable 
- `print("hello world")`

## O(log n)
it will run at a rate equal to the log of the input set size.

### Examples
- divide and conquor
- binary search

## O(n)
it will run at a rate equal to the input set size.

### Examples
- a for loop

## O(n^2)
it will run at a rate equal to the input set size SQUARED.

### Examples 
- a nested for loop
    - O(n^3) would be two nested for loop

```python
# This is O(n^2)
for i in li:
    for j in li:
        print(i, j)

# This is O(n^3)
for x in li:
    for y in li:
        for z in li:
            print(x, y, z)

# This is O(n!)
def func(n):
    for i in range(n):
        func(n-1)
```





# Languages
## W3 languages
## Dynamicly Typed Languages
- inferred and mutable data types
- pros:
    - easy
    - fast
    - generally less verbose
    - lets you do dumb things
- cons:
    - complexity increases as the project scales
    - lets you do dumb things
    - generally slower / less memory efficient
- examples
    - Python
    - Javascript

## Statically Typed Languages
- defined variable types (`string`, `int`, `Class` ...)
- pros:
    - generally faster and more memory efficient
    - less runtime errors as more errors are caught in development
    - complexity is easier to manage
- cons:
    - generally harder / slower to write
    - more syntax errors to deal with
    - generally more concise
- examples
    - Java
    - Typescript
    - C
## Functional
- stateless
- more of a paradigm than a type of language
    - Python, Javascript ... can all be functional so long as you adhere to the functional philosophy
- philosphy: pure functions - no side effects, stateless, same output given the same input
- pros:
    - easier to unit test
- cons:
    - not as widely known and supported

## Object-oriented
- concept of Objects that organize software design around data
- pros: 
    - decreased duplicate logic
- cons:
    - 

```

```
## Scripting

    - Bash
    - Python
## Concurrent Languages
    - GO
## Interpreted 
## Compiled



# Vocabulary 
- mutable
- immutable
- recursion
- instance
- regex
- API
- backend
- frontend
- http

# Resources
- https://www.youtube.com/watch?v=-uleG_Vecis&ab_channel=Fireship

- data structures
    - linked list
        - https://medium.com/@ytsuji91/data-structures-in-javascript-part-1-linked-lists-94301942499d
    - https://www.geeksforgeeks.org/python-data-structures-and-algorithms/
- bash
    - https://kinsta.com/blog/linux-commands/




# TODO
- how to setup VS Code
- file system overview
    - paths
        - relative
        - absolute
        - . / ..
- git