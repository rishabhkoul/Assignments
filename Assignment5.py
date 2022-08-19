"""
1. What does an empty dictionary's code look like?
    An empty dictionary looks like: {}

2. What is the value of a dictionary value with the key 'foo' and the value 42?
    Value of a dictionary {foo:42} is 42

3. What is the most significant distinction between a dictionary and a list?
    The structure of dictionary has a key value pair, while list is a list of indexed elements.
    Dictionary is unordered while list is ordered

4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?
    We get a KeyError as key 'foo' is not present in dictionary spam

5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and
'cat' in spam.keys()?
    There is no difference in both expressions. Both will check if 'cat' is a key in the dictionary


6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and
'cat' in spam.values()?
    The expression 'cat' in spam will only check the keys of the dictionary while the expression 'cat'
    in spam.values() will check only the values of the dictionary

7. What is a shortcut for the following code?
if 'color' not in spam:
    spam['color'] = 'black'
    spam.setdefault('color','black')


8. How do you "pretty print" dictionary values using which module and function?
    we use the pprint module and function called pprint to pretty print a dictionary
   import pprint
   pprint.pprint(dict_name)
"""

import pprint
spam = {'bar':100}
spam2 = {'foo':100,'cats':200,'bar':300,'fad':'cat','Name': 'Jose', 'Age': '44', 'Country': 'Spain'}
print({'foo':42}.values())
#print(spam['foo'])
spam.setdefault('color','black')
print(spam)
pprint.pprint(spam2)