# Assignment 2: 

Description: This program takes two nodes and extracts text from both objects (including their children nodes). Then it compares if the text is the same.   
The object structure of each node is:  
node = {    
    is_text   
    string    
    Children  
}  

This program will use a sample node tree that I created for testing purposes. Please refer to the image that I provided for reference. This tree contains 17 nodes in total. The file nodes.py reflects this tree with the correct is_text, string, and Children fields for each of the nodes.   
There are two sets of nodes with matching strings in this example:    
    node 6 and node 8 (both with a string of ABCDE)  
    node 4 and node 7 (both with a string of WXYZ)  
Every other combination will have mismatching strings.     

To start this program, run this script on your terminal:
```
python assignment2.py
```
You will then be prompted to enter your first node and your second node. The program will print out the resulting strings from each of the nodes and whether they are different or same. 

Demo:
```
> python assignment2.py
Enter the number of the first node you want to compare.
200
Input not valid. Please try again.
4
Enter the number of the first node you want to compare.
a
Input not valid. Please try again.
8
WXYZ
ABCDE
Strings from both nodes are different
```

