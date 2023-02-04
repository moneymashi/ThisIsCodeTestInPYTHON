## https://www.acmicpc.net/problem/2042

n, m, k = 5, 2, 2  #map(int, input("input data...").split())

# 전체 데이터개수
arr = [0] * (n + 1)  # 사용자 숫자. 주의: 수정변동 가능.
tree = [0] * (n + 1)  # BIT: 구간별 합계 저장.


# i번째 수까지 누적합을 계산.
def prefix_sum(i):
  result = 0  # i번쨰까지 누적합.
  while i > 0:
    result += tree[i]  # i번째 관련 BIT 구간합계를 누적.
    # 0이 아닌 마지막비트만큼 빼가면서 이동.
    i -= (i & -i)
  return result


# i번째 수를 dif만큼 더해줌
def update(i, dif):
  while i <= n:
    tree[i] += dif  # 차이만큼 관련 구간합계에도 수정처리.
    i += (i & -i)


# start~end 구간합 계산.
def interval_sum(start, end):
  return prefix_sum(end) - prefix_sum(start - 1)


#for i in range(1, n + 1):
for i in [1, 2, 3, 4, 5]:
  #x = int(input())
  x = i
  arr[i] = x
  update(i, x)  # tree에 구간합 추가. dif = x - 0

#for i in range(m + k):
for a, b, c in [(1, 3, 6), (2, 2, 5), (1, 5, 2), (2, 3, 5)]:
  #a, b, c = map(int, input().split())
  if a == 1:  # 숫자 업데이트.
    update(b, c - arr[b])  # tree에 구간합 추가. dif = c-arr[b]
    arr[b] = c
  elif a == 2:  # 구간합[b,c] 구하기
    print(interval_sum(b, c))
