# Basic Object Oriented Programming in Python

> _NOTE: the acronym OOP will be used in place of "Object-Oriented-Programming" throughout_

**What we'll cover**:

- [What is OOP?](#what-is-oop)
- [Objects in Python](#almost-everything-is-an-object)
- [Where do Objects come from?](#where-do-objects-come-from)
- [A Simple Class](#a-simple-class)
- [Adding Data](#adding-data)
- [Adding Functionality](#adding-functionality)
- [Inheritance](#inheritance)

Python is a [multi-paradigm](https://en.wikipedia.org/wiki/Programming_paradigm) programming language, but OOP is central to Python's design.

This document will guide you through the fundamentals of OOP in Python. This guide assumes you are familiar with basic Python syntax. If you would like to brush up, or if "Python syntax" is something you've never heard before, check out [An Informal Introduction to Python](https://docs.python.org/3/tutorial/introduction.html). I'll also include links to various syntax in the [PythonCheatsheet](https://www.pythoncheatsheet.org) throughout this guide. If you see a word in blue that you don't understand, click it to get more information.

## What is OOP?

From the [Wikipedia page on OOP](https://en.wikipedia.org/wiki/Object-oriented_programming):
_Object-oriented programming (OOP) is a programming paradigm based on the concept of "objects", which can contain data and code: data in the form of fields (often known as attributes or properties), and code, in the form of procedures (often known as methods)._

## (Almost) Everything is an Object

In Python, almost everything is an Object. Here, we make a [list](https://www.pythoncheatsheet.org/cheatsheet/lists-and-tuples) containing [integers](https://www.pythoncheatsheet.org/cheatsheet/basics#data-types) `1`, `2`, and `3`. Then we append the integer `4` to the list:

```python
myList = [1, 2, 3]
myList.append(4)
```

Here, `myList` is an Object the of `list` class. We'll cover classes in a bit.

We know the `myList` Object has **data** in it. `1`, `2`, and `3` are stored somewhere inside `myList`.

We know the `myList` Object has **code** in it. We call a function `append` on `myList`. `append` is a method (or function) that belongs to the `myList` object

## Where do Objects Come From?

Every Object comes from a class. Classes are Object blueprints. Classes describe what an Object is, and classes are used to actually _create_ the Objects they describe. An Object is said to be an **instance** of the class it came from. An instance of the `List` class can also be called a **List object**.

#### A Simple Class

During the next few steps we'll create Objects that can print messages to your [terminal](https://medium.com/@krish.raghuram/terminal-shell-and-bash-3e76218c8865) or [command prompt](https://www.makeuseof.com/tag/a-beginners-guide-to-the-windows-command-line/).

In order to make our own Objects, we'll first need to create a class that describes them. In Python, you create classes using the `class` [keyword](https://en.wikipedia.org/wiki/Reserved_word).

Here is a very simple class, `Message`:

```python
class Message:
    pass
```

The indented section is called the class _body_. Our `Message` class's body contains only the keyword `pass`. Pass tells Python to simply do _nothing_. We've described an object that doesn't contain any **data** or **code**

But we can still create an instance of our `Message` class. We'll call our `Message` object "myMessage":

```python
myMessage = Message()
```

So we've created a message Object, but it doesn't contain any data. Later, we'll modify our class to describe Objects that contain data!

#### The `__init__` method

If you look again at the code `myMessage = Message()` you can can see we called `Message` like it is a [function](https://www.pythoncheatsheet.org/cheatsheet/functions). That's because, behind the scenes, Python _is_ calling a function, and that function is named `Message.__init__`. The `__init__` function is special. It's what's called the class _constructor_. It belongs to the `Message` class and it's used to _construct_ `Message` objects.

> _**Note**: functions that belong to a class are often called **methods**. Going forward, I'll refer to class functions as **methods** in order to distinguish between regular functions and the methods of a class._

Our `Message` class has a constructor even though we didn't actually write one. If we don't define a constructor for our class, Python will create one for us. Behind the scenes, our Class ends up looking something like this:

```python
class Message:
    def __init__(self):
        pass
```

When running the code `myMessage = Message()`, Python calls `Message.__init__()` for us, then it builds a `Message` object which is assigned to `myMessage`.

Calling `Message()` is sort of like calling `Message.__init__()`

You may have noticed something's not right here. When we wrote `myMessage = Message()` we didn't pass any arguments, but `Message__init__` methos expects one argument, `self`. That's because Python automatically passes the _instance_ as the first argument to class methods. It's convention to name that argument "self" because _the argument is an instance of the class itself_

#### Adding Data

`Message.__init__` only contains the `pass` keyword. That's because the constructor Python gives us doesn't do much of anything. In order to construct an Object with some data, we'll have to create our own constructor for our `Message` class!

So, our `Message` class should describe a message. What's in a message? For starters, a message needs content. We can store our message's content in a [String](https://www.pythoncheatsheet.org/cheatsheet/basics#data-types). But first We'll need to give our `Message` class a string to build a `Message` object with.

Let's write our own constructor that takes another argument names `content` and assigns it to `self`

```python
class Message:
    def __init__(self, content):
        self.content = content
```

Remember, `self` is an instance of `Message` -- it is the `Message` Object being constructed. So we set its `content` to the content passed in to the constructor.

Now we can create a `Message` Object that has content:

```python
myMessage = Message("hello world!")
print(myMessage.content) # hello world!
```

Now let's add an author:

```python
class Message:
    def __init__(self, author, content):
        self.author = author
        self.content = content

myMessage = Message("Chris", "myMessage is an instance of the Message class")
print(myMessage.author)  # Chris
print(myMessage.content)  # myMessage is an instance of the Message class
```

#### Adding Functionality

We can add additional functionality to our `Message` class too. Class related functionality provided by methods, just like the `__init__` method described earlier.

Let's add a method to `Message` that prints our message for us:

```python
class Message:
    def __init__(self, author, content):
        self.author = author
        self.content = content

    def print_message(self):
        print(f"{self.author} says {self.content}")

myMessage = Message("Chris", "hello!")
myMessage.print_message() # Chris says hello!
```

## Inheritance

One of the core concepts in OOP is [inheritance](https://www.w3schools.com/python/python_inheritance.asp). Inheritance enables you to create classes that are derived from other classes. The derived class is called a _child_ class, and the class it's derived from is called the _parent_ class. By default, a child class inherits all of the parent class's properties and methods.

In the same file, let's create a `Whisper` class based on our `Message` class:

```python
class Whisper(Message):
    pass
```

Since the `Whisper` class's body only contains the `pass` keyword, you might think `Whisper` can't do anything. However, because `Whisper` inherits from `Message`, it can do all the things the `Message` class can do:

```python
myWhisper = Whisper("Chris", "I've got a secret")
myWhisper.print_message() # Chris says I've got a secret
```

#### Extending the `Message` class

You can customize a child class by [overriding](https://www.geeksforgeeks.org/method-overriding-in-python/) its parent's methods:

```python
class Whisper(Message):
    def print_message(self):
        print(f"{self.author} whispers {self.content}")

myWhisper = Whisper("Chris", "I've got a secret")
myWhisper.print_message() # Chris whispers I've got a secret
```

Here is the whole file:

```python
class Message:
    def __init__(self, author, content):
        self.author = author
        self.content = content

    def print_message(self):
        print(f"{self.author} says {self.content}")

class Whisper(Message):
    def print_message(self):
        print(f"{self.author} whispers {self.content}")


myMessage = Message("Chris", "hello!")
myMessage.print_message() # Chris says hello!

myWhisper = Whisper("Chris", "I've got a secret")
myWhisper.print_message() # Chris whispers I've got a secret
```

#### Overriding the `__init__` method

By default, a child class will have the same constructor as its parent. However, sometimes it makes sense for a child class to have its own constructor.

Say we have a `Rectangle` class:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

myRectangle = Rectangle(10, 5)
rectangleArea = myRectangle.get_area()
print(rectangleArea) # 50
```

And we want to inherit from `Rectangle` to create a `Square` class. Squares _are_ rectangles, but since squares have the same width and height, we should be able to construct a `Square` by providing just the length of its sides.

We can derive a `Square` class with a constructor that takes just one parameter by overriding its `__init__` method. Keep in mind that when we override `__init__`, we need to call the parent's `__init__` method and pass it `self` as well as `side_length` for both `height` and `width`:

```python
class Square(Rectangle):
    def __init__(self, side_length):
        Rectangle.__init__(self, side_length, side_length)

mySquare = Square(5)
squareArea = mySquare.get_area()
print(squareArea) # 25
```

Python provides a shortcut, `super()` which doesn't need the `self` parameter:

```python
class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

mySquare = Square(5)
squareArea = mySquare.get_area()
print(squareArea) # 25
```

> read more about `super()` [here](https://www.geeksforgeeks.org/python-super/)

Here's the full file with an added rectangle object:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

myRectangle = Rectangle(10, 5)
rectangleArea = myRectangle.get_area()
print(rectangleArea) # 50

mySquare = Square(5)
squareArea = mySquare.get_area()
print(squareArea) # 25
```
