"""
https://youtu.be/cswJ1h-How0
# 9. 코딩테스트에서 자주 출제되는 기타 알고리즘.

"""

n = 5  # data 개수
m = 5  # sum 값
data = [1, 2, 3, 2, 5]
count = 0
interval_sum = 0
end = 0

for start in range(n):
  while interval_sum < m and end < n:
    interval_sum += data[end]
    end += 1
  if interval_sum == m:
    count += 1
  # start+1 넘어가기 전, start+1 ~ end 값만 interval_sum에 남겨두기.
  interval_sum -= data[start]

print('two pointer result: ', count)
