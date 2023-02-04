## https://www.acmicpc.net/problem/11657
import sys
INF = int(1e9)

def bf(start):
  dist[start] = 0
  for i in range(n):  # n번 라운드 반복
    for j in range(m):  # 반복마다 모든 간선 확인.
      cur = edges[j][0]
      next_node = edges[j][1]
      cost = edges[j][2]
      # 현재 간선을 거쳐 다른노드로 이동거리가 짧은경우
      if dist[cur] != INF and dist[next_node] > dist[cur] + cost:
        dist[next_node] = dist[cur] + cost
        if i == n - 1:  # n번째 라운드에서 값이 갱신되면 음수순환 존재.
          return True
  return False

# n; 노드, m: 간선개수
#n, m = 3, 4  #map(int, input().split())
n, m = 3, 2

# 최다거리 테이블 모두 무한으로 초기화.
dist = [INF] * (n + 1)
# 모든 간선에 대한 리스트. (a,b,c) = map(int, input().split)
#edges = [(1, 2, 4), (1, 3, 3), (2, 3, -4), (3, 1, -2)]
edges = [(1, 2, 4), (1, 2, 3)]

#bellmanford alg
negative_cycle = bf(1)  # start:1 (시작:노드1)

if negative_cycle:
  print("negative_cycle: -1")
else:
  # 모든 간선에 대한 최단 거리출력.
  for i in range(2, n + 1):
    # == INF -> 도달할수 없음
    if dist[i] == INF:
      print("invalid path: -1")
    else:
      print(dist[i])
