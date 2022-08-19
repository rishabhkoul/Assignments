"""
1. In the below elements which of them are values or an expression? eg:- values can be
integer or string and expressions will be mathematical operators.
    *           Expression
    "hello"     Value
    -87.8       Value
    -           Expression
    /           Expression
    +           Expression
    6           Value

2. What is the difference between string and variable?
    String is a data type which contains a sequence of characters. It can contain alphabets, numbers, symbols etc.
    String values are written in quotes "" or ''.
    Variables on the other hand are used as pointers to a memory location where an object or other value is stored.
    Variables can have different data type depending on the values stored.

3. Describe three different data types.
    String - This data type stores characters which can be letters, numbers or symbols.
    Integer - This data type stores integer values
    Float - This data type stores floating or decimal values

4. What is an expression made up of? What do all expressions do?
    An expression is a combination of values(operands) and operators which results in an output or another value.
    Example of expressions: a+b+25, 150//15 , 25*88/2+59

5. This assignment statements, like spam = 10. What is the difference between an expression and a statement?
    Statements are instructions that are executed in python. They represent an action or command in python.
    Expressions are a combination of operands and operators that result in a value.
    if else is a statement but not an expression. 5*5 + 20*5 is an expressions which results in 125


6. After running the following code, what does the variable bacon contain?
    bacon = 22
    bacon + 1
        After running this code bacon will contain 23 value


7. What should the values of the following two terms be?
    "spam "+ "spamspam"
    "spam * 3"
        Both will give the same output ie. spamspamspam


8. Why is eggs a valid variable name while 100 is invalid?
    100 is an invalid variable name because variable cannot start with a number.
    Variable can only start with a letter or underscore.
    Variable names can contain only alphanumeric characters and underscores.


9. What three functions can be used to get the integer, floating-point number, or string version of a value?
    Let's take an example:
    a = 256.25
    int(a) will give the integer value ie. 256
    float(a) will give the floating point value ie. 256.25
    str(a) will give the string version of the value ie. '256.25'

10. Why does this expression cause an error? How can you fix it?
    "I have eaten" + 99 + "burritos"
        This expression is trying to concatenate a string value('I have eaten') with integer value (99).
        To fix this error we can use the str() function to convert 99 into string value.
        "I have eaten" + str(99) + "burritos"
        The output will be:      I have eaten99burritos

"""
print("spam" + "spamspam")
print("spam" * 3)
print(int(256.36))
print("I have eaten" + str(99) + "burritos")
print(5*5 + 20*5)