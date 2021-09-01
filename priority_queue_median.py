# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
import heapq
import sys

asc_heap = []
dsc_heap = []

n = int(input())

for i in range(n):
    num = int(input())
    if i%2 == 0:
        heapq.heappush(asc_heap, -num)
    else:
        heapq.heappush(dsc_heap, num)
    
    if i >=1:
        if -asc_heap[0] > dsc_heap[0]:
            tmp1 = heapq.heappop(asc_heap)
            tmp2 = heapq.heappop(dsc_heap)

            heapq.heappush(asc_heap, -tmp2)
            heapq.heappush(dsc_heap, -tmp1)
            
    print(-asc_heap[0])
