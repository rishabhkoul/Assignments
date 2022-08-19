"""
1. What exactly is []?
    [] represents a list. A list can contain different values of different data types such as string, integers, float, other lists etc

2. In a list of values stored in a variable called spam, how would you assign the value 'hello' as the
   third value? (Assume [2, 4, 6, 8, 10] are in spam)
        spam[2] = "Hello"

Let's pretend the spam includes the list ['a', 'b', 'c', 'd'] for the next three queries.

3. What is the value of spam[int(int('3' * 2) / 11)]?
    'd'
4. What is the value of spam[-1]?
    'd'

5. What is the value of spam[:2]?
    ['a','b']

Let's pretend bacon has the list [3.14, 'cat', 11, 'cat', True] for the next three questions.
6. What is the value of bacon.index('cat')?
    1

7. How does bacon.append(99) change the look of the list value in bacon?
    The new list would look like this [3.14, 'cat', 11, 'cat', True,99]

8. How does bacon.remove('cat') change the look of the list in bacon?
    [3.14, 11, 'cat', True]

9. What are the list concatenation and list replication operators?
    + operator is used for list concatenation. Example: ['a', 2, 'c'] + ['b', 'd', 23] = ['a', 2, 'c', 'b', 'd', 23]
    * operator is used for list replication. Example:  ['a', 2, 'c'] * 2 = ['a', 2, 'c', 'a', 2, 'c']

10. What is difference between the list methods append() and insert()?
    append() function allows us to add a new element only at the end of the list while
    insert() function allows us to specify the index at which we want to add the new element.

11. What are the two methods for removing items from a list?
    list.delete() remove from specified index
    list.remove() remove the first matching element from a list

12. Describe how list values and string values are identical.
    list and string values are both indexed and iterable

13. What's the difference between tuples and lists?
    lists are mutable while tuples are immutable

14. How do you type a tuple value that only contains the integer 42?
    (42)

15. How do you get a list value's tuple form? How do you get a tuple value's list form?
    To get a tuple form of list we type tuple(list)
    To get a list form of tuple we type list(tuple)

16. Variables that "contain" list values are not necessarily lists themselves. Instead, what do they
contain?
 Variables than contain list values are only references to list values, and they don't actually contain list values.


17. How do you distinguish between copy.copy() and copy.deepcopy()?
    Changes made in copy.copy() will reflect in the original but changes made in deepcopy will not reflect in the original

"""

spam = [2, 4, 6, 8, 10]
spam[2] = "Hello"
print(spam)

bacon = [3.14, 'cat', 11, 'cat', True]
print(bacon.remove('cat'))
print(bacon+spam)

print(['a', 2, 'c'] * 2)
print(type(bacon))