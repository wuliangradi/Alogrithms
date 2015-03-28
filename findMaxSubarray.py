#coding=utf-8

import math
inf = float("inf")

def findMaxCrossingSubarray(A, low, mid, high):
    # 总共n次迭代
    leftSum = -inf
    sum = 0
    maxLeft = 0
    # 这里如果不加这两句声明，for循环里的maxLeft是不能被后面使用的
    maxRight = 0
    for i in range(mid, 0, -1):
        sum = sum + A[i]
        if sum > leftSum:
            leftSum = sum
            maxLeft = i

    rightSum = -inf
    sum = 0
    for j in range(mid+1, high):
        sum = sum +A[j]
        if sum > rightSum:
            rightSum = sum
            maxRight = j

    return maxLeft, maxRight, leftSum+rightSum

def findMaxSubarray(A, low, high):
    if high==low:
        return(low, high, A[low])
    # 到“基本情况”的判断条件
    else:
        mid = int(math.floor((low + high)/2))
        (leftLow, leftHigh, leftSum) = findMaxSubarray(A, low, mid)
        # 这里有一个小细节，如果求解左侧最值时没包括mid，这样在求解包括中间的最值时会很不好办
        (rightLow, rightHigh, rightSum) = findMaxSubarray(A, mid+1, high)
        (crossLow, crossHigh, crossSum) = findMaxCrossingSubarray(A, low, mid, high)
        if leftSum >= rightSum and leftSum >= crossSum:
            return (leftLow, leftHigh, leftSum)
        elif rightSum >= leftSum and rightSum >= leftSum:
            return (rightLow, rightHigh, rightSum)
        else:
            return (crossLow, crossHigh, crossSum)

A = [-13, -3, -25, -20, -3, -16, -23, -18, -20, -7, -12, -5, -22, -15, -4, -7]
# 当所有数为负数时，返回的时 1，1，-3，即最大的负数
re = findMaxSubarray(A, 0, len(A)-1)
print re



