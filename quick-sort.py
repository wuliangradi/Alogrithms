#coding=utf-8


def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i = i +1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)

A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7, 55, 66, 23, -3, 8]
quicksort(A, 0, len(A)-1)

# 这些想法太帅了
# A[r]主元
# 还可以使用随机选择主元的方法，将选中元素与尾元素交换