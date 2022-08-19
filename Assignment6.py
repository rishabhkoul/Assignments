"""
1. What are escape characters, and how do you use them?
    Escape characters are used to insert illegal characters inside a string.
    example to use double quotes inside double quots we can escape the quotes inside the string.
    a = "This is a "demo" sentence"         # This line of code will give an error
    a = "This is a \"demo\" sentence"       # This code fixes the problem by escaping the character

2. What do the escape characters n and t stand for?
    Escape character 'n' stands for new line
    and 't' stands for tab
    These are used to insert new line or tab separator inside a string.
    Example: "Second line starts here.\nThis is the \tsecond line"


3. What is the way to include backslash characters in a string?
    To include backslash character we can escape it using backlash.
    example: "To escape backlash we use \\"


4. The string "Howl's Moving Castle" is a correct value. Why isn't the single quote character in the
word Howl's not escaped a problem?
    We can use single quotes inside a double quoted string.
    We however cannot use single quotes inside single quoted string and similarly double quotes inside a
    double quoted string.

5. How do you write a string of newlines if you don't want to use the n character?


6. What are the values of the given expressions?
'Hello, world'[1]        = 'e'
'Hello, world'[0:5]      = 'Hello'
'Hello, world'[:5]       = 'Hello'
'Hello, world'[3:]       = 'lo, world'


7. What are the values of the following expressions?
'Hello'.upper()                 = 'HELLO'
'Hello'.upper().isupper()       = True
'Hello'.upper().lower()         = 'hello'

8. What are the values of the following expressions?
'Remember, remember, the fifth of July'.split()    = ['Remember,', 'remember,', 'the', 'fifth', 'of', 'July']
'-'.join('There can only one.'.split())            = There-can-only-one.


9. What are the methods for right-justifying, left-justifying, and centering a string?
    str.rjust() for right justifying
    str.ljust() for left justifying
    str.center() for centring a string

10. What is the best way to remove whitespace characters from the start or end?
    str.strip()  function can be used to remove whitespace from both ends.
    str.lstrip() function can be used to remove whitespace from left end.
    str.rstrip() function can be used to remove whitespace from rigth end.

"""

print("This is a \"demo\" sentence")
print("Second line starts here.\nThis is the \tsecond line" )
print("To escape backlash we use \\")
print("Next line")

print('Hello, world'[1],
'Hello, world'[0:5],
'Hello, world'[:5],
'Hello, world'[3:])

print('Hello'.upper() ,
'Hello'.upper().isupper() ,
'Hello'.upper().lower())

print('Remember, remember, the fifth of July'.split() )
print('-'.join('There can only one.'.split()))

print('Hello, world'.rjust(20,'x'))
print('Hello, world'.ljust(20,'x'))
print('Hello, world'.center(20,'x'))

print('   hello   '.strip())
print('   hello   '.lstrip())
print('   hello   '.rstrip())

