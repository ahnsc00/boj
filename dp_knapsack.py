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
#dp

n, weight = map(int, input().split())
wt = []
val = []
for i in range(n):
    w, v = map(int, input().split())
    wt.append(w)
    val.append(v)

def knapsack(W, wt, val, n): # W: 배낭의 무게한도, wt: 각 아이템 무게, val: 각 아이템 가격, n: 아이템 수
    K = [[0 for x in range(W+1)] for x in range(n+1)]
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                K[i][w] = 0
                
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1]+K[i-1][w-wt[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    return K[n][W]

print(knapsack(weight, wt, val, n))
# -



