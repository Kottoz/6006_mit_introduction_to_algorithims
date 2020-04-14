
#  * @author Kotoz
#  * @email mohamed.t.elshetry@mail.com
#  * @create date 2020-04-14 00:40:29
#  * @modify date 2020-04-14 00:40:29
#  * @desc [Find Maxsimuim subarray using divide and conquer approach]
 
def find_maximum_cross(A, low, mid, high):
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
