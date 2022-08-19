"""
1.What are the two values of the Boolean data type? How do you write them?
    Two values of Boolean data type are True and False or 0 and 1
    In python 1 is written as True and 0 as False

2. What are the three different types of Boolean operators?
    Three types of boolean operators are AND, OR, NOT

3. Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean
values for the operator and what it evaluate ).
    0 and 0 = 0      0 or 0 = 0     not 0 = 1
    0 and 1 = 0      0 or 1 = 1     not 1 = 0
    1 and 0 = 0      1 or 0 = 1
    1 and 1 = 1      1 or 1 = 1

4. What are the values of the following expressions?
    (5 > 4) and (3 == 5)        0 False
    not (5 > 4)                 0 False
    (5 > 4) or (3 == 5)         1 True
    not ((5 > 4) or (3 == 5))       0 False
    (True and True) and (True == False)     0 False
    (not False) or (not True)       1 True

5. What are the six comparison operators?
    Six comparison operators are:
    >       greater than
    <       less than
    ==      equal to
    >=      greater than or equal to
    <=      less than or equal to
    !=      not equal to

6. How do you tell the difference between the equal to and assignment operators?Describe a condition and when you would use one.
    Equal to operator is used to compare two values and give a boolean value as output
    But assignment operator is used to assign values or point to a variable
    If we want to compare the values of two variable we will use equal to operator.
     a == b if a and b are equal the output will be True
     if we want to assign value to a variable we will use assignment operator. Example
     a = 258, b = 45, c = a+b


7. Identify the three blocks in this code:
spam = 0                1st block

if spam == 10:          2nd block
    print('eggs')

if spam > 5:            3rd block
    print('bacon')
else:
    print('ham')
    print('spam')
    print('spam')


8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints
Greetings! if anything else is stored in spam.
    if spam == 1:
        print("Hello")
    elif spam == 2:
        print("Howdy")
    else:
        print("Greetings!")


9.If your programme is stuck in an endless loop, what keys you’ll press?
    ctrl + c


10. How can you tell the difference between break and continue?
    break keyword terminates the execution of the current loop and passes the control to the next loop or main body,
    but the continue keyword just skips the current iteration of the loop and executes the next iteration

11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?
    range(10) - In this function only upper limit is given so this function will generate a range from 0 to 10 excluding 10.
    range(0,10) - In this function both lower and upper limits are given so this function will generate
     a range from lower limit 0 to upper limit 10 excluding 10.
    range(0,10,1) - In this function lower limit, upper limit and step is given so this function will generate
     a range from 0 to 10 excluding 10 with a step size of 1.

12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent
program that prints the numbers 1 to 10 using a while loop.
    for i in range(1,11):
        print(i)

    i = 1
    while i < 10:
        print(i)
        i +=1


13. If you had a function named bacon() inside a module named spam, how would you call it after
importing spam?
    spam.bacon()


"""