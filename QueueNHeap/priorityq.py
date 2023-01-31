import sys
import heapq

input = sys.stdin.readline


# minHeap sorting w/ list.
def heapsort(iterable, bAsc):
  h = []
  result = []
  ascVal = (1 if bAsc else -1)  # 1: asc, -1: desc.
  # 모든원소 차례대로 힙에 삽입
  for v in iterable:
    heapq.heappush(h, v * ascVal)  # default: minHeap
  for i in range(len(h)):
    result.append(ascVal * heapq.heappop(h))
  return result


n = 10  #int(input())
arr = [3, 5, 2, 4, 1, 8, 7, 9, 0, 6]

res = heapsort(arr, True)
print('res(ASC): ', res)

res = heapsort(arr, False)
print('res(DESC): ', res)
