class Node:
  def __init__(self, data, left_node, right_node):
    self.data = data
    self.left_node = left_node
    self.right_node = right_node


# pre_order: 부모노드 -> 왼쪽노드 -> 우측노드
def pre_order(node):
  print(node.data, end=" ") ## 전위순회 data 출력
  if node.left_node != None:
    pre_order(tree[node.left_node])
  if node.right_node != None:
    pre_order(tree[node.right_node])


# in_order: 왼쪽노드 -> 부모노드 -> 우측노드
def in_order(node):
  if node.left_node != None:
    in_order(tree[node.left_node])
  print(node.data, end=" ") ## 중위순회 data 출력
  if node.right_node != None:
    in_order(tree[node.right_node])

# post_order: 우측노드 -> 부모노드 -> 좌측노드
def post_order(node):
  if node.left_node != None:
    post_order(tree[node.left_node])
  if node.right_node != None:
    post_order(tree[node.right_node])
  print(node.data, end=" ") ## 후위순회 data 출력


# 데이터 입력받기.
n = 7  #int(input())
tree = {} #dict.
list = [('A', 'B', 'C'), ('B', 'D', 'E'), ('C', 'F', 'G'), ('D', None, None),
        ('E', None, None), ('F', None, None), ('G', None, None)]
for data, left_node, right_node in list:
  tree[data] = Node(data, left_node, right_node)

print('pre_order: ', end=" ")
pre_order(tree['A'])
print()

print('in_order: ', end=" ")
in_order(tree['A'])
print()

print('post_order: ', end=" ")
post_order(tree['A'])
print()
