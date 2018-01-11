#-*- coding: utf8 -*-

#파이썬에는 '리스트 컴프리헨션'이라는 한 리스트에서 다른 리스트를 만들어내는 간결한 문법이 있다.

# 각 숫자의 제곱 계산값들이 저장된 리스트를 예로 들어보자
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x**2 for x in a]
print(squares)

# 인수가 하나뿐인 함수를 적용하는 상황이라면 lambda를 사용하는 것이 좋다.
squares = map(lambda  x: x**2, a)

# 하지만, 인자를 두 개 이상을 사용할 때는 깔끔해보이지 않기 때문에 리스트 컴프리헨션을 사용하는 것이 좋다.
# (리스트컴프리헨션을 사용하면) map과 달리 리스트 컴프리헨션을 사용하면 입력리스트에 있는 아이템을 편하게 걸러내서 이에 대응하는 출력을 결과에서 삭제할 수 있다.
# 예제로 차이점을 확인해보자
# 리스트 컴프리헨션을 사용한 예제
#even_squares = [x**2 for x in a if x%2 == 0]
even_squares = [x for x in a if x%2 == 0]
print('even: {}', even_squares)

#내장함수 filter를 map과 연계한 예제를 보자
alt = map(lambda x: x**2, filter(lambda x: x%2 == 0, a))
assert even_squares == list(alt)

# 딕셔너리와 세트에도 리스트 컴프리헨션에 해당하는 문법이 있다.
# 컴프리헨션 문법을 쓰면 알고리즘을 작성할 때 파생되는 자료구조를 쉽게 생성할 수 있다.
chile_ranks = {'ghost':1, 'habanero':2, 'cayenne': 3}
rank_dict = {rank: name for name, rank in chile_ranks.items()}
chile_len_set = {len(name) for name in rank_dict.values()}
print(rank_dict)
print(chile_len_set)
