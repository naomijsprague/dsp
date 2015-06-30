# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

[![Think Python](img/think_python.png)](http://www.greenteapress.com/thinkpython/)

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

Complete the following exercises to check your ability with Python.

These exercises are implemented with doctests, which are runnable tests inside docstrings. Fill in the function definitions. Correct solutions will make it possible to run (for example) `python -m doctest strings.py` with no messages about failures.

 * [Strings](python/strings.py)
 * [Lists](python/lists.py)


---

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

* Lists are mutable, tuples are immutable. Tuples will work as keys in dictionaries.

---


---

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?
>
* Sets can't contain duplicates
* Sets are unordered
* In order to find an element in a set, a hash lookup is used (which is why sets are unordered). This makes __contains__ (in operator) a lot more efficient for sets than lists.
* Sets can only contain hashable items (see #3). If you try: set(([1],[2])) you'll get a TypeError.

```
mylist=[5, 25, 3, 400, 21, 25, 5]

print type(mylist)
print len(mylist)

myset= set(mylist)
print type(myset)
print len(myset)
print myset
```

--- 


---
Describe Python's 'lambda'. What is it, and what is it used for? Give at least one example, including an example of using a 'lambda' in the 'key' argument to 'sorted'.
>
Python supports the creation of anonymous functions (i.e. functions that are not bound to a name) at runtime, using a construct called "lambda". Creates a temporary function.


```
def f (x): return x**2

print f(8)


g = lambda x: x**2 

print g(8)

def get_kg(pounds): return pounds/2.2046

print get_kg(75)

g = lambda pounds: pounds/2.2046 

print g(75)

```

---


---

Explain list comprehensions. Give examples and show equivalents with 'map' and 'filter'. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

REPLACE THIS TEXT WITH YOUR RESPONSE

---


Write a Markov text generator, [markov.py](python/markov.py). Your program should be called from the command line with two arguments: the name of a file containing text to read, and the number of words to generate. For example, if 'chains.txt' contains the short story by Frigyes Karinthy, we could run:

```bash
./markov.py chains.txt 40
```

A possible output would be:

> show himself once more than the universe and what I often catch myself playing our well-connected game went on. Our friend was absolutely correct: nobody from the group needed this way. We never been as the Earth has the network of eternity.

There are design choices to make; feel free to experiment and shape the program as you see fit. Jeff Atwood's [Markov and You](http://blog.codinghorror.com/markov-and-you/) is a fun place to get started learning about what you're trying to make.
