# Assignment 1:   

Description: This program takes an integer amount and any number of coin denonimations in any order. It returns the minimum coins that are needed to create the specified integer amount. 

To start the program, run this script on your terminal:  
```
python assignment1.py
```

You will then be prompted to enter an array of integers. Enter 0 when you are done inputting all your numbers. A list of the coins that you entered will be displayed. 
Then, you will be prompted to enter the amount that you want to break your change in. The number will be printed out again to confirm. 

Demo of an input with an answer:  
```
> python assignment1.py
Enter all your coin denominations. Enter 0 when you are done.
-1
Input not valid (you may have entered an invalid character or a negative number). Please try again.
a
Input not valid (you may have entered an invalid character or a negative number). Please try again.
1
2
5
0
Your coins:
1 2 5

Enter the integer amount you want your coins to add up to.
11
Your coin value: 11


The coins that make up your solution are:
1 5 5
```

Demo of an input with no answer: 
```
> python assignment1.py  
Enter all your coin denominations. Enter 0 when you are done.
2
4
6
0
Your coins:
2 4 6

Enter the integer amount you want your coins to add up to.
13

No solution
```
