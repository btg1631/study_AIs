py_list = [[1,2]
           ,[3,4]
           ,[5,6]]  # list
import numpy as np
np_array = np.array([[7, 8]
                    ,[9,10]
                    ,[11,12]])  # 행렬 = array

pass  


# 구분 위한 type 확인
type(py_list)
# <class 'list'>
type(np_array)
# <class 'numpy.ndarray'>

# class type에 따른 편리성
py_list.sum()
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
# AttributeError: 'list' object has no attribute 'sum'
np_array.sum()
# 57

np_array.sum(axis=0)  # row 단위 연산
# array([27, 30])
np.sum(np_array, axis=0)
# array([27, 30])

np_array.sum(axis=1)  # column 단위 연산
# array([15, 19, 23])
np.sum(np_array, axis=1)
# array([15, 19, 23])

# 병합
np_array_second = np.array(py_list)
type(np_array_second)
# <class 'numpy.ndarray'>
np.concatenate((np_array, np_array_second), axis=0)  # row 단위 병합
# array([[ 7,  8],
#        [ 9, 10],
#        [11, 12],
#        [ 1,  2],
#        [ 3,  4],
#        [ 5,  6]])
np.concatenate((np_array, np_array_second), axis=1)  # column 단위 병합
# array([[ 7,  8,  1,  2],
#        [ 9, 10,  3,  4],
#        [11, 12,  5,  6]])
