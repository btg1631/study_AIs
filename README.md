# ✏️ study_AIs

## ☑ 사용기술
<img alt="이미지명" src ="https://img.shields.io/badge/PYTHON-3776AB.svg?&style=for-the-badge&logo=PYTHON&logoColor=white"/> <img alt="이미지명" src ="https://img.shields.io/badge/visual studio code-007ACC.svg?&style=for-the-badge&logo=visualstudiocode&logoColor=white"/> <img alt="이미지명" src ="https://img.shields.io/badge/google colab-F9AB00.svg?&style=for-the-badge&logo=googlecolab&logoColor=white"/>


## 💻 머신러닝(Machine learning)
- 기계가 일일이 코드로 명시하지 않고 동작을 데이터로부터 학습하여 실행할 수 있도록 하는 알고리즘 분야(Artuur Samuel)

|*|제목|code|설명|비고|
|--|--|--|--|--|
|0|numpys|[numpys](./docs/MLs/numpys.py)|기초문법 모음|||
|1|로지스틱 회귀|[LogisticRegression](./docs/MLs/classfications/01_LogisticRegression_simple.ipynb)|||
|2|군집화|[clustering](./docs/MLs/clusterings/01_clustering_simple.ipynb)|||
|3|선형 회귀|[linearRegression](./docs/MLs/Regression/01_linearRegression_simple.ipynb)|||


## 💻 자연어 처리(Natural Language Processing)
- 컴퓨터에게 인간과 매우 유사한 방식으로 텍스트 및 음성 언어를 이해하는 능력을 부여하는 것과 관련된 컴퓨터 공학의 한 분야

|*|제목|code|설명|비고|
|--|--|--|--|--|
|1|wordcloud 기본|[wordcloud_simple](./docs/NLPs/wordcloud_simple.py)|기본(영어) wordcloud 분석|||
|2|wordcloud 한글|[wordcloud_korean](./docs/NLPs/wordcloud_korean.ipynb)|||
|3|정규표현식(regexp)|[wordcloud_korean_regexp](./docs/NLPs/wordcloud_korean_regexp.ipynb)|정규표현식 사용하여 복잡한 문자열 처리||
|4|Okt, Mecab|[morphemes](./docs/NLPs/morphemes.ipynb)|Okt, Mecab활용 형태소 분리|||
|5|wordcloud Mecab|[wordcloud_mecab](./docs/NLPs/wordcloud_korean_mecab.ipynb)|Mecab활용 wordcloud|||
|6|tokenizer|[wordcloud_tokenizers](./docs/NLPs/wordcloud_korean_tokenizers.ipynb)|토큰화|||


## 📚 QUEST
|*|구분|code|설명|비고|
|--|--|--|--|--|
|1|MLs|[RentalCarOfContractType](./docs/quests/MLs/RentalCarOfContractType.ipynb)|linear regression 사용, age 결측치 처리||
|2|MLs|[SpineSurgeryList_FeatureEngin](./docs/quests/MLs/SpineSurgeryList_FeatureEngin.ipynb)|목표변수(재발여부), 설명변수(수치형 5개, 범주형 2개)||
|3|MLs|[SpineSurgeryList_GridSearchCV_resampling](./docs/MLs/SpineSurgeryList_GridSearchCV_resampling.ipynb)|linear regression 사용, age 결측치 처리|resampling 종류에 따른 F1 score 변화 관찰|
|4|NLPs|[wordcloud_regexp](./docs/NLPs/wordcloud_regexp.ipynb)|Oneword Game을 wordcloud 표현|본인 작성 내용만 변환(values(list) 활용), 상위 30단어만 표시|
|5|NLPs|[classification_news](./docs/NLPs/classification_news.ipynb)|IT News를 카테고리화, 카테고리 wordcloud 표시|학습된 모델을 pickle로 불러옴|
|6|NLPs|[classification_movies](./docs/NLPs/classification_movies.ipynb)|영화 댓글에 대한 감성분석|classification_report로 model 성능 확인|



