# -*- coding: utf-8 -*-
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
#brute-force

N, weight = map(int, input().split())
items = []
for i in range(count):
    x, y = map(int, input().split())
    items.append([x, y])
    
W = 0
V = 1

def knapsack(pos,weight):
    if (pos == N): return 0

    ret = 0
    
    if (items[pos][W] <= weight): #지금 pos의 물건을 넣을 수 있을 때
        ret = knapsack(pos + 1, weight - items[pos][W]) + items[pos][V]
    
    #지금 pos의 물건을 넣지 않을때와 ret 중에 큰 값
    ret = max(ret, knapsack(pos + 1, weight))
    return ret
    

print("knapsack({0},{1})={2}\n".format(0, weight, knapsack(0, weight)))

