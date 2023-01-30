"""
https://youtu.be/cswJ1h-How0
# 9. 코딩테스트에서 자주 출제되는 기타 알고리즘.

"""
import math


# 복잡도: O(x)
def is_prime_number_old(x):
  for i in range(2, x):
    if x % i == 0:
      return False
  return True


# 복잡도: O(sqrt(x))
def is_prime_number(x):
  for i in range(2, int(math.sqrt(x) + 1)):
    if x % i == 0:
      return False
  return True


# 에라토스테라스의 체
def eratosteras(x):
  array = [True for i in range(x + 1)]  # 1~x 소수 초기화.
  for i in range(2, int(math.sqrt(x) + 1)):
    if array[i] == True:  # i 가 소수인경우.
      j = 2
      while i * j <= x:  # i 배수는 모두 False처리.
        array[i * j] = False
        j += 1
  list = []  # 소수 idx 리스트.
  for idx in range(2, x + 1):
    if array[idx]:
      list.append(idx)
  return list
