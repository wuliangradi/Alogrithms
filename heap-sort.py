#coding=utf-8
import math

def parent(i):
    return int(math.floor((i-1)/2))

def left(i):
    return 2*i+1

def right(i):
    return 2*i+2

def maxHeapify(A, i):
    l = left(i)
    r = right(i)
    if l <= heapsizeA and A[l]>A[i]:
        largest = l
    else:
        largest = i
    if r <= heapsizeA and A[r]>A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        maxHeapify(A, largest)


def buildMaxHeap(A):
    # 这里range负方向downto这里-1是它的下限，但到不了-1
    for i in range(int(math.floor(heapsizeA/2)), -1, -1):
        maxHeapify(A, i)


def heapsort(A):
    buildMaxHeap(A)
    for i in range(len(A)-1, 0, -1):
        A[i], A[0] = A[0], A[i]
        heapsizeA = heapsizeA - 1
        maxHeapify(A, 0)


A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
heapsizeA = len(A)-1
heapsort(A)

# 构造最大堆是关键。然后就是一个取出最大堆里的第一个元素（肯定是最大）。然后不断构造最大树。
