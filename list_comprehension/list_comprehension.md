
[참조](https://en.wikipedia.org/wiki/List_comprehension)

1. 리스트 컴프리헨션이란..
==========================
파이썬에는 '리스트 컴프리헨션'이라는 한 리스트에서 다른 리스트를 만들어내는 간결한 문법이 있다.
간단한 예제로 사용법을 확인해보자
[syntax](./list_comprehension_syntax.svg)
~~~python
# regular list comprehension
a = [(x, y) for x in range(1, 6) for y in range(3, 6)]
# [(1, 3), (1, 4), (1, 5), (2, 3), (2, 4), ...
~~~


2. map, filter와의 차이
========================
조건식이나 수식이 더 복잡해지게 되면 map, filter보다는 컴프리헨션을 사용하는 것이 더 간결하다.
아래 예제를 보면 map과 달리 리스트 컴프리헨션을 사용하면 입력리스트에 있는 아이템을 편하게 걸러내서 이에 대응하는 출력을 결과에서 삭제하는 것을 볼 수 있다.

(리스트 컴프리헨션)
~~~python
even_num = [x**2 for x in a if x%2 == 0]
~~~

(내장함수 filter를 map과 연계)
~~~python
alt = map(lambda x: x**2, filter(lambda x: x%2 == 0, a))
assert even_squares == list(alt)
~~~


3. 딕셔너리에도 컴프리헨션 문법이 있다
=======================================
딕셔너리와 세트에도 리스트 컴프리헨션에 해당하는 문법이 있다.
컴프리헨션 문법을 쓰면 알고리즘을 작성할 때 파생되는 자료구조를 쉽게 생성할 수 있다.
~~~python
>>> s = {key: val for key, val in enumerate('ABCD') if val not in 'CB'}
>>> s
{0: 'A', 3: 'D'}
>>>
~~~


4. C++등 다른 언어에도 컴프리헨션 문법이 있다고 한다.. 
=====================================================
[wiki](https://en.wikipedia.org/wiki/List_comprehension)