간혹 파일에 데이터를 쓸때 바이너리로 쓰는 것이 필요할 때가 있다..
이를 위해서는 binary 데이터로 인코딩하고 string으로 decoding하는 방법이 필요하다.
다음은 이에 대한 예제임

Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> byte_str = b'hahaha'

>>> print(byte_str)
b'hahaha'

>>> byte_str.decode('utf-8')
'hahaha'

>>> str_str = 'hahahahaha'
>>> print(str_str)
hahahahaha

>>> str_str.encode('utf-8')
b'hahahahaha'
>>>
