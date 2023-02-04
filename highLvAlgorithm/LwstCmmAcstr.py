n = 15  #int(input())
parent = [0] * (n + 1)  #부모노드 정보
d = [0] * (n + 1)  # 각 노드까지 깊이
c = [0] * (n + 1)  # 각 노드의 깊이 계산여부 확인.
graph = [[] for _ in range(n + 1)]  # 그래프 정보

n_list = [(1, 2), (1, 3), (2, 4), (3, 7), (6, 2), (3, 8), (4, 9), (2, 5), (5, 11), (7, 13), (10, 4), (11, 15), (12, 5), (14, 7)]
#for _ in range(n - 1):
for a, b in n_list:
  #a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)  ## ??
print('1st graph:', graph)

def dfs(x, depth):
  c[x] = True  # 계산여부확인.
  d[x] = depth  # 깊이정보
  for y in graph[x]:
    if c[y]:  # 이미 깊이가 있는경우 패스
      continue
    parent[y] = x
    dfs(y, depth + 1)


#최소 공통 조상 찾기
def lca(a, b):
  # 깊이(depth)를 일치화.
  while d[a] != d[b]:
    if d[a] > d[b]:
      a = parent[a]
    else:
      b = parent[b]
  # 공통부모 찾을때까지 부모노드로 올라감.
  while a != b:
    a = parent[a]
    b = parent[b]
  return a


dfs(1, 0)  # 루트노드는 1.
print('parent:', parent)
print('depth:', d)
print('calc:', c)

m = 6  #int(input())

m_list = [(6, 11), (10, 9), (2, 6), (7, 6), (8, 13), (8, 15)]

#for i in range(m):
for a, b in m_list:
  #a, b = map(int, input().split())
  print('lca({},{}): {}'.format(a,b, lca(a, b)))
