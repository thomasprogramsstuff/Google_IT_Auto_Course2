##Now, you may have noticed that most of the Python code samples we've used include the line 

#!/usr/bin/env python3

#Now, this is important, because it sets the Python version to Python 3.

#There are some subtle differences in how data streams are handled in Python 3 and older versions, such as Python 2. Let’s just focus on input() and raw_input(), because they work differently in Python 2 and 3, and you would want to use one or the other depending on the Python version.

###!!!In PYTHON 2###!!!

#Taking an input from a user, raw_input should be used:

##BASH##
>>> my_number = raw_input('Please Enter a Number: \n')
Please Enter a Number: 
1337
>>> print(my_number)
1337
>>>

#Now, this is important, because, raw_input does not evaluate an otherwise valid Python expression. 
#In simple terms, raw_input will just get a string from a user, where input will actually perform basic maths and the like. See below:

>>> my_raw_input = raw_input('Please Enter a Number: \n')
Please Enter a Number: 
123 + 1  # This is treated like a raw string.
>>> my_input = input('Please Enter a Number: \n')
Please Enter a Number: 
123 + 1 # This is treated like an expression.
>>> print(my_raw_input)
123 + 1
>>> print(my_input)
124 # See that the expression was evaluated!

##In Python 2 input(x) is just eval(raw_input(x)). eval() will just evaluate a generic string as if it were a Python expression.

###!!!In PYTHON 3###!!!

#Taking an input from a user, input should be used. See the below sample:

>>> my_number = input('Please Enter a Number: \n')
Please Enter a Number: 
123 + 1
>>> print(my_number)
123 + 1
>>> type(my_number)
<class 'str'>

#Notice that the expression is treated just like a string. It is not evaluated. 
#If we want to, we can call eval() and that will actually execute the string as an expression:

#>>> my_number = input('Please Enter a Number: \n')
Please Enter a Number: 
123 + 1
>>> print(my_number)
123 + 1
>>> eval(my_number)
124
