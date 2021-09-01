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
for i in range(count):
    w, v = map(int, input().split())
    wt.append(w)
    val.append(v)

def knapsack(W, wt, val, n):  # W: 배낭의 무게한도, wt: 각 보석의 무게, val: 각 보석의 가격, n: 보석의 수
    K = [[0 for x in range(W+1)] for x in range(n+1)]  # DP를 위한 2차원 리스트 초기화
    for i in range(n+1):
        for w in range(W+1):  # 행 기준 각 칸을 돌면서
            if i==0 or w==0:  # 0번째 행/열은 0으로 세팅
                K[i][w] = 0
                
            elif wt[i-1] <= w:  #첫 번째 보석이 무게보다 작다면
                # 첫 번째 보석의 가치 + n번째 보석이 포함되지 않은 개수(행)현재 무게에 첫 번째 보석의 무게를 뺀 무게(열)
                # 첫 번째 보석을 포함 안했을 때 가장 큰 가치
                K[i][w] = max(val[i-1]+K[i-1][w-wt[i-1]], K[i-1][w])  # max 함수 사용하여 큰 것 선택
            else:
                # n번째 보석이 포함되지 않은 무게와 똑같은 값
                K[i][w] = K[i-1][w]
    return K[n][W] # for문이 끝나고 마지막 값 출력

print(knapsack(weight, wt, val, n))
