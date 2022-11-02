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

### 네이버 영화 리뷰 및 평점 수집하기

#### 네이버 영화 폄점 사이트에서 특정 영화("헤어질 결심")을 검색 후 다양한 정보를 수집하는 크롤러 만들기

<img width="1800" alt="스크린샷 2022-11-02 오후 5 04 02" src="https://user-images.githubusercontent.com/72393144/199433327-cb5fe7c9-4bd8-458f-a4da-bca6fe3c35e1.png">
여기에서 별점, 리뷰내용, 작성자, 작성일자, 공감수와 비공감수의 정보를 가져오는 크롤러를 만든 후
<img width="1800" alt="스크린샷 2022-11-02 오후 5 04 13" src="https://user-images.githubusercontent.com/72393144/199433355-4966ecf2-673a-40e1-92f5-8b7016640712.png">

텍스트 파일과 엑셀 파일을 만들어 볼 것이다

```python
# 연습문제 :네이버 영화 리뷰 모으기

# Step 1. 필요한 모듈과 라이브러리를 로딩합니다.

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

import time
import sys
import math
import numpy
import pandas as pd
import os
import random

print("=" * 80)
print("연습문제 :네이버 영화 리뷰 정보 수집하기 ")
print("=" * 80)

query_txt = input('1.크롤링 할 영화의 제목을 입력하세요: ')
query_url = 'https://movie.naver.com'

cnt = int(input('2.크롤링 할 리뷰건수는 몇건입니까?: '))
page_cnt = math.ceil(cnt / 10)

f_dir='/Users/gimhagyeong/Desktop/파이썬1급/'

# 저장될 파일위치와 이름을 지정합니다
now = time.localtime()
s = '%04d-%02d-%02d-%02d-%02d-%02d' % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
os.makedirs(f_dir+s+'-'+query_txt)
os.chdir(f_dir+s+'-'+query_txt)

ff_name=f_dir+s+'-'+query_txt+'\\'+s+'-'+query_txt+'.txt'
fc_name=f_dir+s+'-'+query_txt+'\\'+s+'-'+query_txt+'.csv'
fx_name=f_dir+s+'-'+query_txt+'\\'+s+'-'+query_txt+'.xlsx'

# Step 3. 크롬 드라이버를 사용해서 웹 브라우저를 실행합니다.
s_time = time.time()


s = Service("/Users/gimhagyeong/Downloads/chromedriver")
driver = webdriver.Chrome(service=s)

driver.get(query_url)
time.sleep(2)

# 영화 제목으로 검색
element = driver.find_element(By.ID,"ipt_tx_srch")
element.send_keys(query_txt)
driver.find_element(By.XPATH,'//*[@id="jSearchArea"]/div/button').click()
driver.find_element(By.XPATH,'//*[@id="old_content"]/ul[2]/li/dl/dt/a').click()


        
# Step 4 평점 옵션 버튼 클릭
driver.find_element(By.LINK_TEXT,"평점").click()


# Step 5. 현재 페이지 리뷰와 점수 등 내용 수집
# IFRAME 변경
driver.switch_to.frame('pointAfterListIframe')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# 현재 총 리뷰 건수를 확인하여 사용자의 요청건수와 비교 후 동기화
result = soup.find('div', class_='score_total').find('strong', 'total').find('em').get_text()

print("=" * 80)
search_cnt = int(result.replace(",", ""))

if cnt > search_cnt:
    cnt = search_cnt

print("전체 검색 결과 건수 :", search_cnt, "건")
print("실제 최종 출력 건수", cnt)

print("\n")
page_cnt = math.ceil(cnt / 10)
print("크롤링 할 총 페이지 번호: ", page_cnt)
print("=" * 80)


score2 = []
review2 = []
writer2 = []
wdate2 = []
gogam2 = []
g_gogam2 = []
b_gogam2 = []
dwlist2 = []

count = 0         # 크롤링 건수 카운트 변수
click_count = 1   # 페이지 번호


while ( click_count <= page_cnt )  :
            
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            
            score_result = soup.find('div', class_='score_result').find('ul')
            slist = score_result.find_all('li')

            for li in slist:

                count += 1
                
                f = open(ff_name, 'a',encoding='UTF-8')
            
                print("\n")
                print("총 %s 건 중 %s 번째 리뷰 데이터를 수집합니다==============" %(cnt,count))
                score = li.find('div', class_='star_score').find('em').get_text()
                print("1.별점:","*"*int(score),": ", score)
                score2.append(score)
                f.write("\n")
                f.write("총 %s 건 중 %s 번째 리뷰 데이터를 수집합니다==============" %(cnt,count) + "\n")
                f.write("1.별점:"+score + "\n")
            
                review = li.find('div', class_='score_reple').find('p').get_text().replace('\n','').strip()
                print("2.리뷰내용:",review)
                f.write("2.리뷰내용:" + review + "\n")
                review2.append(review)
         
                dwlist = li.find('div',class_='score_reple').find_all('em')
                writer = dwlist[0].find('span').get_text()
                print("3.작성자:",writer)
                f.write("3.작성자:" + writer + "\n")
                writer2.append(writer)
                
                wdate = dwlist[1].text
                print('4.작성일자:',wdate)
                f.write("4.작성일자:" + wdate + "\n")
                wdate2.append(wdate)
            
                gogam = li.find('div', class_='btn_area').find_all('strong')
                g_gogam = gogam[0].text
                print('5.공감:',g_gogam)
                f.write("5.공감:" + g_gogam + "\n")
                g_gogam2.append(g_gogam)
                
                b_gogam = gogam[1].text
                print('6.비공감:', b_gogam)
                f.write("6.비공감:" + b_gogam + "\n")
                b_gogam2.append(b_gogam)
                
                if count == cnt :
                    break
            
            time.sleep(random.randrange(1,2))  

            click_count += 1
            
            if click_count > page_cnt :
                break
            else :
                driver.find_element(By.LINK_TEXT,"%s" %click_count).click()

            time.sleep(random.randrange(1,2))  # 3-8 초 사이에 랜덤으로 시간 선택

#Step 11. xls 형태와 csv 형태로 저장하기
naver_movie = pd.DataFrame()
naver_movie['별점(평점)']=score2
naver_movie['리뷰내용']=review2
naver_movie['작성자']=writer2
naver_movie['작성일자']=wdate2
naver_movie['공감횟수']=g_gogam2
naver_movie['비공감횟수']=b_gogam2

# csv 형태로 저장하기
naver_movie.to_csv(fc_name,encoding="utf-8-sig",index=True)

# 엑셀 형태로 저장하기
naver_movie.to_excel(fx_name ,index=True,engine='openpyxl')

e_time = time.time( )
t_time = e_time - s_time

print("\n") 
print("=" *80)
print("1.요청된 총 %s 건의 리뷰 중에서 실제 크롤링 된 리뷰수는 %s 건입니다" %(cnt,count))
print("2.총 소요시간은 %s 초 입니다 " %round(t_time,1))
print("3.파일 저장 완료: txt 파일명 : %s " %ff_name)
print("4.파일 저장 완료: csv 파일명 : %s " %fc_name)
print("5.파일 저장 완료: xls 파일명 : %s " %fx_name)
print("=" *80)

driver.close( )
```

### 결과

엑셀 파일 데이터 <br/><br/>
<img width="1048" alt="스크린샷 2022-11-02 오후 5 01 10" src="https://user-images.githubusercontent.com/72393144/199434876-8674ac7b-22dd-46d0-88ec-b4e4500af015.png">
<br/><br/>
텍스트 파일 데이터
<img width="1103" alt="스크린샷 2022-11-02 오후 5 01 31" src="https://user-images.githubusercontent.com/72393144/199434931-001d623e-729d-41b3-aebf-cb5f239ccca6.png">


