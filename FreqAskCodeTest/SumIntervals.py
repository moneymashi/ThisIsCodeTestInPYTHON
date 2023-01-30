"""
https://youtu.be/cswJ1h-How0
# 9. 코딩테스트에서 자주 출제되는 기타 알고리즘.

"""

## 구간 합
n = 5
data = [10, 20, 30, 40, 50]

#접두사 합
sum_value = 0
prefix_sum = [0]  # 초기 배열에 0 원소는 기본.
for i in data:
  sum_value += i
  prefix_sum.append(sum_value)  # 접두사합을 계속 append.

#구간 합 계산
left = 3
right = 4
print('interval_sum: ', prefix_sum[right] - prefix_sum[left - 1])
