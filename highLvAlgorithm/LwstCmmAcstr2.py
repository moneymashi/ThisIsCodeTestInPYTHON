n = 15  #int(input())
LOG = 21 # 2^20 = 1000000.

#부모노드 정보 + 각 노드의 조상부모 정보.
parent = [[0] * LOG for _ in range(n + 1)]  ### ++++
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
    parent[y][0] = x
    dfs(y, depth + 1)

# 전체 부모관계를 설정하는 함수
def set_parent():
  dfs(1, 0) # 루트노드.
  for i in range (1,LOG) :
    for j in range(1, n+1) :
      parent[j][1] = parent[parent[j][i-1]][i-1]
    
#최소 공통 조상 찾기
def lca(a, b):
  # b가 더 깊도록 설정
  if d[a] > d[b]:
    a,b = b,a
  # 깊이가 동일하게 거슬러 올라가게 처리.
  for i in range(LOG-1, -1, -1):
    if d[b] - d[a] >= (1 << i) : ## ??
      b = parent[b][i]
  # 공통부모 찾을때까지 부모노드로 올라감.
  if a == b:
    return a
  # 조상을 향해 거슬러 올라가기.
  for i in range(LOG-1, -1, -1) :
    if parent[a][i] != parent[b][i] :
      a = parent[a][i]
      b = parent[b][i]
  return parent[a][0]

dfs(1, 0)  # 루트노드는 1.
print('parent:', parent)
print('depth:', d)
print('calc:', c)

set_parent()
m = 6  #int(input())
m_list = [(6, 11), (10, 9), (2, 6), (7, 6), (8, 13), (8, 15)]
for a, b in m_list:
  print('lca({},{}): {}'.format(a,b, lca(a, b)))
