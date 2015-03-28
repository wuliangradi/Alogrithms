#coding=utf-8
import math


def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = [A[p+i] for i in range(n1)]
    R = [A[q+j+1] for j in range(n2)]
    L.append(float("inf"))                  # 这个inf哨兵很厉害，能减少很多工作
    R.append(float("inf"))
    i = 0
    j = 0
    for k in range(p, r):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1

def merge2(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = [A[p+i] for i in range(n1)]
    R = [A[q+j+1] for j in range(n2)]
    i = 0
    j = 0
    for k in range(p, r):
        if i >= n1:
            A[k:r] = R[j:n2-1]
            break
        if j >= n2:
            A[k:r] = L[i:n1-1]
            break
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1

def mergeSort(A, p, r):
    if p < r:
        q = int(math.floor((p+r)/2))
        mergeSort(A, p, q)
        mergeSort(A, q+1, r)
        merge2(A, p, q, r)
    return A

A = [2, 4, 5, 7, 1, 2, 3, 6]
A = mergeSort(A, 0, len(A)-1)
print A