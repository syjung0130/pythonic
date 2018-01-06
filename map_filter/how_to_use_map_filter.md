파이썬에서는 리스트를 더 편리하고 간결한 방식으로 사용할 수 있도록 map, filter와 같은 내장함수를 제공한다.

참조링크: [reference link](http://book.pythontips.com/en/latest/map_filter.html)

이 함수들은 한 리스트에서 특정 표현식, 조건식으로 필요한 값을 뽑아낼 수 있도록 도와준다.

for문을 사용해서 구현을 해도 되지만, 이 함수들을 사용하면 더욱 간결한 방법으로 구현할 수 있다.

예제로 확인해보는 것이 이해가 빠를 것 같다.



1.map
===========

map의 기본적인 표현식은 다음과 같다.

적용할 함수(첫번째 인자)와 입력이 되는 list(두번째 인자)를 parameter로 사용하고 있다.

(첫번째 인자로는 대부분 lamda와 같은 표현식을 사용한다.)

~~~python
map(function_to_apply, list_of_inputs)
~~~

우선, 한 리스트의 원소들의 제곱을 한 리스트를 출력하는 알고리즘을 for문을 이용해서 구현한 코드를 보자


~~~python
items = [1,2,3,4,5]
squared = []
for i in items:
    squared.append(i**2)
print('squared(using for loop): {}'.format(squared))
~~~


출력결과는 다음과 같다.
squared(using for loop): [1, 4, 9, 16, 25]


이번에는 map을 사용해서 구현한 코드를 보자
훨씬 더 간결한 코드로 바뀐 것 같다.


~~~python
items = [1,2,3,4,5]
squared = []
squared = list(map(lambda x: x**2, items))
~~~
print('squared(using lambda, map): {}'.format(squared))

출력결과는 다음과 같다.
squared(using lambda, map): [1, 4, 9, 16, 25]


이번에는 document의 예제를 살펴보자

map을 사용해서 0~4까지의 숫자를 [제곱, 두배]쌍의 리스트로 생성하는 것으로 보인다.


lambda를 통해서 0~4까지의 값을 funcs의 에 들어가고 있고
funcs라는 리스트는 함수들이 원소로 구성되어있다.

funcs의 원소들에 0~4까지의 값들을 넘겨주게 될것이고
funcs의 원소들인 함수에 0~4까지의 값들이 전달되게 된다.
결국 출력은 [제곱, 두배]의 쌍이 출력되게 된다..
~~~python
def multiply(x):
    return (x*x)
def add(x):
    return (x+x)
 
funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)
 
# Output:
# [0, 0]
# [1, 2]
# [4, 4]
# [9, 6]
# [16, 8]
~~~

흠..리스트에 함수가 들어갈 수 있다는 건 처음 알았다.
이것도 다음에 한번 알아보기로 하자
음.. 역시 공식문서의 예제가 다른 블로그나 튜토리얼 사이트보다 더 얻을 것이 많은 것 같다..


2.filter
==========
filter는 특정 조건을 만족하는 값들만 걸러내는 것이고, map은 특정 표현식으로 값을 생성하는 것이다.
map과 filter를 같이 사용하면 더 간결한 코드를 작성할 수 있는 것 같다.
위에서 작성했던 제곱값 리스트(squared) 를 얻어오는 예제를 재활용해서 filter를 어떻게 사용하는지 확인해보자..

~~~python
more_than_nine = list(filter(lambda x: x>9, squared))
print('more_than_nine: {}'.format(more_than_nine))
~~~

출력결과는 다음과 같다.
more_than_nine: [16, 25]

