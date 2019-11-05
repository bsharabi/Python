# Getting started with Python
The `>>>` means that Python is ready and we can enter a command. The
basic idea is really simple: we enter a command, press Enter, enter
another command, press Enter and keep going.


## Comments

**Comments are text that does nothing.** They can be created by typing a
`#` and then some text after it, and they are useful when our code would
be hard to understand without them.

```python
>>> 1 + 2     # sum 1 and 2
3
>>>
```

The space after the `#` and multiple spaces before it are just to
make things easier to read.

If we write a comment on a line with no code on it, the prompt changes
from `>>>` to `...`. The prompt goes
back to `>>>` when we press Enter again.

```python
>>> # hello there
...
>>>
```

## Strings

We can create strings by simply writing some text in quotes.

```python
>>> 'hello'
'hello'
>>> 'this is a test'
'this is a test'
>>> 
```

Strings can also be written with "double quotes" instead of 'single
quotes'. This is useful when we need to put quotes inside the string.

```python
>>> "hello there"
'hello there'
>>> "it's test"
"it's test"
>>> 
```

Strings can be joined together easily with `+` or repeated with `*`:

```python
>>> "hello" + "world"
'helloworld'
>>> "hello" * 3
'hellohellohello'
>>> 
```

## Using Python as a calculator

Let's type some math stuff into Python and see what it does.

```python
>>> 17 + 3
20
>>> 17 - 3
14
>>> 17 * 3
51
>>> 17 / 3
5.666666666666667
>>>
```

It's working, Python just calculates the result and echoes it back.

Things are calculated in the same order as in math. The parentheses `(`
and `)` also work the same way.

```python
>>> 1 + 2 * 3        # 2 * 3 is calculated first
7
>>> (1 + 2) * 3      # 1 + 2 is calculated first
9
>>>
```


## Using print

In Python, `print` is just showing text on the screen.

```python
>>> print('Hello!')
Hello!
>>>
```


## Handy things about print

We can also print an empty line by calling print without any
arguments.

```python
>>> print()

>>>
```

In Python, `\n` is a newline character. Printing a string that contains
a newline character also prints a newline:

```python
>>> print('hello\nworld')
hello
world
>>>
```

If we want to print a real backslash, we need to **escape** it by typing
two backslashes.
```python
    >>> print('hello\\nworld')
    hello\nworld
    >>>
```

We can also pass multiple arguments to the print function. We need to
separate them with commas and print will add spaces between them.

```python
>>> print("Hello", "World!")
Hello World!
>>>
```

Unlike with `+`, the arguments don't need to be strings.

```python
>>> print(42, "is an integer, and the value of pi is", 3.14)
42 is an integer, and the value of pi is 3.14
>>>
```



# Variables, Booleans and None

## Variables

Variables are easy to understand. They simply **point to values**.

```python
>>> a = 1   # create a variable called a that points to 1
>>> b = 2   # create another variable
>>> a       # get the value that the variable points to
1
>>> b
2
>>>
```
We can also change the value of a variable after setting it.

```python
>>> a = 2    # make a point to 2 instead of 1
>>> a
2
>>>
```

Setting a variable to another variable gets the value of the other
variable and sets the first variable to point to that value.

```python
>>> a = 1
>>> b = a  # this makes b point to 1, not a
>>> a = 5
>>> b      # b didn't change when a changed
1
>>>
```

Trying to access a variable that is not defined creates an error
message.

```python
>>> thingy
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'thingy' is not defined
>>>
```

Variables are simple to understand, but there are a few details that we
need to keep in mind:

- Multiple variables can point to the same value, but one variable
  cannot point to multiple values.


Variables are an important part of most programming languages, and they
allow programmers to write much larger programs than they could write
without variables.

Variable names are case-sensitive, like many other things in Python.

```python
>>> thing = 1
>>> THING = 2
>>> thIng = 3
>>> thing
1
>>> THING
2
>>> thIng
3
>>>
```

There are also words that cannot be used as variable names
because they have a special meaning. They are called **keywords**, and
we can run `help('keywords')` to see the full list if we want to.
Trying to use a keyword as a variable name causes a syntax error.

```python
>>> if = 123
  File "<stdin>", line 1
    if = 123
       ^
SyntaxError: invalid syntax
>>>
```

When assigning something to a variable using a `=`, the right side of
the `=` is always executed before the left side. This means that we can
do something with a variable on the right side, then assign the result
back to the same variable on the left side.

```python
>>> a = 1
>>> a = a + 1
>>> a
2
>>>
```

To do something to a variable (for example, to add something to it) we
can also use `+=`, `-=`, `*=` and `/=` instead of `+`, `-`, `*` and
`/`. The "advanced" `%=`, `//=` and `**=` also work.

```python
>>> a += 2          # a = a + 2
>>> a -= 2          # a = a - 2
>>> a *= 2          # a = a * 2
>>> a /= 2          # a = a / 2
>>>
```

This is not limited to integers.

```python
>>> a = 'hello'
>>> a *= 3
>>> a += 'world'
>>> a
'hellohellohelloworld'
>>>
```

## Booleans

There are two Boolean values, True and False. In Python, and in many
other programming languages, `=` is assigning and `==` is comparing.
`a = 1` sets a to 1, and `a == 1` checks if a equals 1.

```python
>>> a = 1
>>> a == 1
True
>>> a = 2
>>> a == 1
False
>>>
```

`a == 1` is the same as `(a == 1) == True`, but `a == 1` is more
readable, so most of the time we shouldn't write `== True` anywhere.

```python
>>> a = 1
>>> a == 1
True
>>> (a == 1) == True
True
>>> a = 2
>>> a == 1
False
>>> (a == 1) == True
False
>>>
```

## None

None is Python's "nothing" value. It behaves just like any other value,
and it's often used as a default value for different kinds of things.
Right now it might seem useless but we'll find a bunch of ways to use
None later.

None's behavior on the interactive prompt might be a bit confusing at
first:

```python
>>> thingy = None
>>> thingy
>>>
```

Typing `thingy` didn't echo back None.
This is because the prompt never echoes back None. 

If we want to see a None on the interactive prompt, we can use print.

```python
>>> print(thingy)
None
>>>
```

## Other comparing operators

So far we've used `==`, but there are other operators also. This list
probably looks awfully long, but it's actually quite easy to learn.

| Usage     | Description                       | True examples         |
|-----------|-----------------------------------|-----------------------|
| `a == b`  | a is equal to b                   | `1 == 1`              |
| `a != b`  | a is not equal to b               | `1 != 2`              |
| `a > b`   | a is greater than b               | `2 > 1`               |
| `a >= b`  | a is greater than or equal to b   | `2 >= 1`, `1 >= 1`    |
| `a < b`   | a is less than b                  | `1 < 2`               |
| `a <= b`  | a is less than or equal to b      | `1 <= 2`, `1 <= 1`    |

We can also combine multiple comparisons. This table assumes that a and
b are Booleans.

| Usage     | Description                               | True example                      |
|-----------|-------------------------------------------|-----------------------------------|
| `a and b` | a is True and b is True                   | `1 == 1 and 2 == 2`               |
| `a or b`  | a is True, b is True or they're both True | `False or 1 == 1`, `True or True` |

```python
>>> a=True
>>> b=False
>>> a or b
True
>>> a and b
False
```

`not` can be used for negations. If `value` is True, `not value` is
False, and if `value` is False, `not value` is True.

There's also `is`, but don't use it instead of `==` unless you know
what you are doing. We'll learn more about it later.
