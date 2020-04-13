"""
 * @author Kotoz
 * @email mohamed.t.elshetry@mail.com
 * @create date 2020-04-14 00:38:59
 * @modify date 2020-04-14 00:38:59
 * @desc [Find Maximum subarray using bruteForce algorithim, 
 *        this algorithim is O(n^2)]
"""


def find_max_subArray(array):
    best_sum = float('-inf')
    for i in range(len(array)):
        sum = 0
        for j in range(i, len(array)):
            sum += array[j]
            if sum > best_sum:
                best_sum = sum
    return best_sum 
    
# def find_max_subArray(array):
#     dic = {}
#     sum = 0
#     best_sum = float('-inf')
#     for i in range(len(array)):
#         sum = sum + array[i]
#         dic[str(i)] = sum
#         if sum > best_sum :
#             best_sum = sum
#     sum = 0 
#     for index in range(len(array)):
#         dic[str(index)]
        


arr = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
d = find_max_subArray(arr)
print(d)