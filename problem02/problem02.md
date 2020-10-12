# Problem 02

## Problem Description

The Collatz conjecture states that for any positive integer, if you
repeatedly apply a set of operations to it, it will eventually be
equal to 1. For an integer $n$, these options are:

* if $n$ is even, $f(n) = n / 2$.
* if $n$ is odd, $f(n) = 3n + 1$.

We continue to apply this function until $f(n) = 1$. For example, here
is the case where $n = 9$.

$$
f(9)  = 28
f(28) = 14
f(14) = 7
f(7)  = 22
f(22) = 11
f(11) = 34
f(34) = 17
f(17) = 52
f(52) = 26
f(26) = 13
f(13) = 40
f(40) = 20
f(20) = 10
f(10) = 5
f(5)  = 16
f(16) = 8
f(8)  = 4
f(4)  = 2
f(2)  = 1
$$

If you count that up, we had to apply the function 19 times to get to
the number $1$. We can call this the **total stopping time** of $n$. 

Write a Python program that finds the total stopping time for some
positive integer $n$. Then, use that program to find the total
stopping time for the number 129.

## Key Python Skills

### Functions

In math, a function is something that takes some input and produces
some output. For example, the function $f(x) = 2x$ takes some input $x$
and multiplies it by $2$. Functions in programming languages are
similar. They take 0 or more inputs, perform some computation on them,
and produce 0 or more outputs. In Python, we could write $f(x) as
follows:

```python
def f(x):
    return 2*x
```

The first thing to note here is how to declare a function. We type the
word `def`, followed by the name of the function, followed by its
arguments (inputs) in parentheses, followed by a colon. If I had a
function with multiple inputs, I would declare it like this:

```python
def add_two_numbers(a, b):
    return a + b
```

The other important thing here is the `return` statement. This tells
the function to exit and give the thing to its right as a value. If I
were to use the functions, it would look like this:

```python
x = 4
y = f(x) # y now has the value of 8

a = 2
b = 3
c = add_two_numbers(a, b) # c now has the value of 5
```

Note that you can write comments in your Python code with `#`. Python
will ignore anything in your code after that. Lastly, functions can
have more than one line of code for more complicated calculations.

```python
def is_even(x):
    if (x % 2 == 0):
        return True
    else:
        return False
```

## `while` loops

Last week, you learned about `for` loops, which let you repeat some
code for each item in some range. Another type of loop is `while`,
which repeats your code while some condition is true. For example,
this code continues to increment a number until it is too large.

```python
n = 0

while n < 5:
    n = n + 1

print(n) # this will print 5
```

The condition is checked at the beginning of each entrance into the
loop.
