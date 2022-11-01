# Web Crawling using numpy and pandas

Python library인 **Beautiful Soup**와 **Selenium**를 이용해 웹 크롤링을 한 후에  
**numpy**와 **pandas**를 이용해 액셀 파일이나 텍스트 파일인 .xlsm이나 .csv로 만드는 프로젝트입니다.


## Numpy란?
Numpy는 다차원 배열을 쉽게 처리하고 효율적으로 사용할 수 있도록지원하는 파이썬의 패키지입니다.  
NumPy는 데이터 구조 외에도 수치 계산을 위해 효율적으로 구현된 기능을 제공합니다.  
데이터 분석을 할때, Pandas와 함께 자주 사용하는 도구로 등장합니다.

### numpy를 이용해 2차원 리스트를 변수에 넣기
```python
import numpy as np

arr4 = np.array([[10,20,30],[40,50,60],[70,80,90],[100,110,120]])
print(arr4)
```

결과
```
[[ 10  20  30]
 [ 40  50  60]
 [ 70  80  90]
 [100 110 120]]
 ```
 
 
 ## Pandas란?

Pandas는 쉽고 직관적인 관계형 또는 분류된 데이터로 작업 할 수 있도록 설계된  
빠르고 유연하며 표현이 풍부한 데이터 구조를 제공하는 Python 패키지입니다.

### pandas를 이용해 표 만들기

```python
import pandas as pd

no = ['1번','2번','3번']
name = ['홍길동','전우치','강감찬']
birth = ['1975','','1982']

member6 = pd.DataFrame()
member6['번호'] = no
member6['이름'] = name
member6['생일'] = birth

member6
```

결과

순서|번호|이름|생일
---|---|---|---|
0|1번|홍길동|1975
1|2번|전우치|
2|3번|강감찬|1982


### seaborn library를 이용한 그래프 그리기

#### relplot으로 그래프 그리기
```python
import pandas as pd
import seaborn as sns

tips = sns.load_dataset('tips')
sns.relplot(x='total_bill', y='tip', data=tips, hue="smoker", style="smoker")

```

결과


![1fd2d5f1-572c-470a-a82b-1e8964274a0e](https://user-images.githubusercontent.com/72393144/199147179-ea4c964c-742c-49c6-8109-743aa1ebcc40.png)

#### heatmap으로 그래프 그리기

```python
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

flights = sns.load_dataset('flights')
flights = flights.pivot('month', 'year', 'passengers')
plt.figure(figsize=(10, 10))
ax = sns.heatmap(flights, annot=True, fmt='d', linewidths=.5)
```

![d24ad3f6-ded6-4e3b-aa29-acb6bced7397](https://user-images.githubusercontent.com/72393144/199148216-5dd9d690-c88b-4c0f-bade-1264fa70c39f.png)


## Beautiful Soup로 원하는 웹사이트의 값 추출 후 저장히기

