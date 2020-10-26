# Problem 03

In this problem, you will get a feel for how
to work with the Numpy library, as well as how
to accept user inputs. Your challenge this week
is to write a program to solve a system of linear
equations, as specified by the user. You should
first ask the user how many variables the equation
has, and then ask for the coefficients, then use
Numpy to solve and display the results.

## Example Execution

An example run of the program could look like this:

```
How many variables:  2
Equation 1, Coefficient 1: 1
Equation 1, Coefficient 2: 0
Equation 1, Coefficient 3: 3
Equation 2, Coefficient 1: 0
Equation 2, Coefficient 2: 1
Equation 2, Coefficient 3: 4

Variable 1: 3
Variable 2: 4
```

In this run, we had the following system
of equations:

$$
1*x + 0*y = 3
0*x + 1*y = 4
$$

We can represent this using matrices as:

```python
[[1, 0, 3],
 [0, 1, 4]]
```

## Getting User Input

In Python, it is easy to get input from the user.
The `input` function works like this:

```python
val = input("Message")
```

It will prompt the user for input with the text "Message",
and store a string containing the output in `val`.

## Python Lists

Lists are a powerful data structure which can be used
to store collections of information. Arrays can be
"indexed" to get the values at a current index, and 
values can be added, removed, or modified. Here are
a few examples.

```python
> my_array = [3,4,5]
> print(my_array)
[3,4,5]

> print(my_array[1])
4

> my_array.append(6)
> print(my_array)
[3,4,5,6]
```

Also, note that you can have arrays of arrays to simulate
matrices or any higher-order collections of points.

## Basic Numpy

Numpy is the Python library which works with mathy stuff
like matrices and arrays. It is great for linear algebra,
among other things.

To import the library, do this:

```python
import numpy as np
```

Here are some useful functions for this assignment:

* `np.array(list)` - converts a list into a Numpy array
* `np.zeros(size)` - creates a Numpy array filled with
zeros of a given size
* `np.linalg.solve()` - solves a linear system of equations
represented with matrices as $Ax = b$
