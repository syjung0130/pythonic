슬라이싱이란 시퀀스(리스트, 튜플 등의 자료형)을 잘게 자른다는 의미이고

[start:end]의 같은 방식으로 필요한 범위만큼을 슬라이싱해서 값을 가져올 수 있게 해준다.

슬라이싱을 사용할 때 스트라이드(stride: 간격)을 설정하면 매 n번째 값을 가져올 수 있다.



예를 들어, 스트라이드를 쓰면 리스트에서 홀수와 짝수 인덱스를 그룹으로 묶을 수 있다.

(리스트 원소들이 아름답군요.. 코딩할 맛 나네요~)

sy:6.Pythonic sy$ python3

Python 3.6.0a2 (v3.6.0a2:378893423552, Jun 13 2016, 14:44:21) 

[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin

Type "help", "copyright", "credits" or "license" for more information.

>>> girls = ['설현', '선미', '아이유', '유인나', '서지혜']

>>> girls

['설현', '선미', '아이유', '유인나', '서지혜']



>>> first = girls[::2]

>>> second = girls[1::2]

>>> 

>>> print(first)

['설현', '아이유', '서지혜']

>>> print(second)

['선미', '유인나']

>>> 





stride를 start, end 인덱스와 함께 사용하면 가독성이 떨어진다.

stride를 사용해야 한다면 start와 end 인덱스는 생략하는 것이 좋다.


stride를 start와 end 인덱스와 함께 사용해야 한다면


stride를 적용한 결과를 다른 변수에 할당해서 사용하는 것이 좋다..



전 역시 그래도 설현이..

>>> temp = girls[::2]

>>> temp

['설현', '아이유', '서지혜']

>>> temp[1:-1]

['아이유']

>>>

>>> temp[0:1]


['설현']
