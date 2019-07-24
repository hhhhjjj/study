class Solution:
    def searchMatrix(self, matrix, target):
        # an empty matrix obviously does not contain `target` (make this check
        # because we want to cache `width` for efficiency's sake)
        # 这个用指针移动的方法是确实厉害
        # 当前值大于目标值就向上减小，当前值小于目标值就向右移动，这个起点就设置在最右下角的地方
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        # cache these, as they won't change.
        height = len(matrix)
        width = len(matrix[0])

        # start our "pointer" in the bottom-left
        row = height - 1
        col = 0

        while col < width and row >= 0:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else:  # found it
                return True

        return False

# 这个换成三个矩阵的方法还是不行，还是有bug，在右上角的矩阵
# 看了下答案，还是要划分成四个矩阵，中间的值是左上矩阵的最大值，也是右下矩阵的最小值，所以只需要迭代剩下两个矩阵就行了
#         middle_raw = matrix[len(matrix)//2]
#         middle = middle_raw[len(middle_raw)//2 - 1]
#         if len(matrix) == 1 and len(matrix[0]) == 1:
#             if target == middle:
#                 return True
#             else:
#                 return False
#         else:
#             if target < matrix[0][0]:
#                 return False
#             elif target < middle:
#                 new_matrix = []
#                 try:
#                     for i in range(len(matrix)//2 + 1):
#                         new_matrix.append(matrix[i][0:len(matrix)//2 + 1])
#                     return self.searchMatrix(new_matrix, target)
#                 except:
#                     for i in range(len(matrix)//2):
#                         new_matrix.append(matrix[i][0:len(matrix)//2 + 1])
#                     return self.searchMatrix(new_matrix, target)
#             elif target == middle:
#                 return True
#             elif target > middle and target > middle_raw[len(middle_raw) - 1]:
#                 new_matrix = []
#                 for i in range(len(matrix)//2 + 1, len(matrix)):
#                     new_matrix.append(matrix[i])
#                 return self.searchMatrix(new_matrix, target)
#             else:
#                 new_matrix = []
#                 for i in range(len(matrix)//2 + 1):
#                     new_matrix.append(matrix[i][len(matrix[0])//2:])
#                 return self.searchMatrix(new_matrix, target)
#
#
print(Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],5))

# 递归的要记得return
# 判断空矩阵不能用is，要用==