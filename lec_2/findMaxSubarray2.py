
#  * @author Kotoz
#  * @email mohamed.t.elshetry@mail.com
#  * @create date 2020-04-14 00:40:29
#  * @modify date 2020-04-14 00:40:29
#  * @desc [Find Maxsimuim subarray using divide and conquer approach]
 
def MaxCrossSubarray(A, low, mid, high):
    #left side
    sum = 0 
    left_sum = float('-inf')
    for i in range(mid,low-1, -1):
        sum += A[i]
        if sum > left_sum:
            left_sum = sum 
            best_left = i
    # return left_sum , best_left
    #right side 
    sum = 0 
    right_sum = float('-inf')
    for j in range(mid+1, len(A)):
        sum += A[j]
        if sum > right_sum:
            right_sum = sum
            best_right = j
    return best_left, best_right, left_sum+right_sum
def FindMaxSubarray(array, low, high):
    if high == low :
        return (low, high, array[low])
    else:
        mid = (high+low)//2 
        leftLow, leftHigh, leftSum = FindMaxSubarray(array, low, mid)
        rightLow, rightHigh, rightSum = FindMaxSubarray(array, mid+1, high)
        crossLow, crossHigh, crossSum = MaxCrossSubarray(array, low, mid, high)
        if leftSum >= rightSum and leftSum >=crossSum:
            return (leftLow, leftHigh, leftSum)
        elif rightSum >= leftSum and rightSum >=crossSum:
            return (rightLow, rightHigh, rightSum)
        else:
            return (crossLow, crossHigh, crossSum)

array = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
low = 0 
high = len(array)-1
low, high, sum = FindMaxSubarray (array, low, high) 
#print(low, high, sum)