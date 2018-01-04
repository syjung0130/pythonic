tring, list, tuple과 같은 자료형을 말한다.
파이썬에서는 이런 자료형을 잘라서 조각으로 만들 수 있는 '슬라이싱(slicing)'이라는 문법을 제공한다.

슬라이싱의 기본적인 형태는 list[start:end]의 형태이고,
start인덱스는 포함, end 인덱스는 제외된다.
start인덱스는 0부터 시작 end인덱스는 -1부터 시작하는 식이다.

예제로 확인해보자..
Last login: Wed Dec 27 23:07:15 on ttys000

Python 3.6.0a2 (v3.6.0a2:378893423552, Jun 13 2016, 14:44:21) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> greeting = 'Hello World~~'
>>> print(greeting[:4])
Hell
>>> print(greeting[-4:])
ld~~
>>> print(greeting[3:-3])
lo Worl
>>> 
>>> 
>>> 
>>> greeting[:]
'Hello World~~'
>>> greeting[:5]
'Hello'
>>> greeting[:-1]
'Hello World~'
>>> greeting[4:]
'o World~~'
>>> greeting[-3:]
'd~~'
>>> greeting[2:5]
'llo'
>>> greeting[2:-1]
'llo World~'
>>> greeting[-3:-1]
'd~'


>>> len(greeting)
13
>>> greeting[:13]
'Hello World~~'
>>> greeting[-13:]
'Hello World~~'


>>> greeting[13]
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
IndexError: string index out of range

