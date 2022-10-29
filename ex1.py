import numpy as np
from numpy import nan as NA
import pandas as pd

# data1 = [1, 2, 3, 4, 5]
# array1 = np.array(data1)
# print(array1)

# print(array1.shape)

# y = np.ones((3, 4), dtype=np.int16)
# print(y)

# x = np.linspace((0, 99, 100), dtype=np.int16)
# print(x)

array6 = np.arange(12).reshape(3, 4)
# print(array6)

# array7 = np.arange(12)
# print(array7)


array7 = array6.reshape(2, 6)
# print(array7)

array8 = array6.reshape(-1, 2)
# print(array8)


array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])
# print('-vstack', np.vstack((array1, array2)))
# print('-hstack', np.hstack((array1, array2)))
# print(np.column_stack((array1, array2)))

name = np.array(['a', 'b', 'c', 'd'])
num = np.array([1, 2, 3, 4])

# print(np.column_stack((name, num)))

# print(array1+array2)

array1 = np.random.randn(3, 3)
# print(array1)


member3 = {'번호': [1, 2, 3], '이름': ['홍길동', '김길동', '박길동'], '나이': [20, 30, 40]}
member3_df = pd.DataFrame(member3, columns=['번호', '나이', '이름'])
# print(member3_df)
# print(member3_df[0:2])

no = [1, 2, 3]
name = ['홍길동', '김길동', '박길동']
birth = [1992, 1993, 1994]

member6 = pd.DataFrame({'번호': no, '이름': name, '생년': birth})
# print(member6.sort_values(by='생년', ascending=True))
# print(member6.loc[(member6['생년'] > 1992) & (member6['번호'] > 1), ['이름', '생년']])

member8 = pd.DataFrame(member6, columns=['번호', '이름', '생년', '성별'])
member8['성별'] = ['남', '여', '남']
# print(member8)


member9 = {'번호': [1, 2, 3, 4, 5, 6, 7],
           '이름': ['홍길동', '김길동', 'NA', '이길동', '최길동', 'NA', '윤길동'],
           '나이': [20, 30, 40, NA, 60, NA, 80]}
member10 = pd.DataFrame(member9, columns=['번호', '이름', '나이'])
print(member10)
