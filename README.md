# 『밑바닥부터 시작하는 딥러닝』

<a href="http://www.yes24.com/Product/Goods/34970929"><img src="https://github.com/WegraLee/deep-learning-from-scratch/blob/master/cover_image.jpg" width="200" align=right></a>

:red_circle: **[공지]** 종종 실습용 손글씨 데이터셋 다운로드 사이트( http://yann.lecun.com/exdb/mnist/ )가 연결되지 않습니다.
그래서 예제 수행에 필요한 데이터셋 파일을 /dataset/ 디렉터리에 올려뒀습니다.
혹 사이트가 다운되어 데이터를 받을 수 없다면 아래 파일 4개를 각자의 <예제 소스 홈>/dataset/ 디렉터리 밑에 복사해두면 됩니다. ^__^

* [t10k-images-idx3-ubyte.gz](https://github.com/WegraLee/deep-learning-from-scratch/raw/master/dataset/t10k-images-idx3-ubyte.gz)
* [t10k-labels-idx1-ubyte.gz](https://github.com/WegraLee/deep-learning-from-scratch/raw/master/dataset/t10k-labels-idx1-ubyte.gz)
* [train-images-idx3-ubyte.gz](https://github.com/WegraLee/deep-learning-from-scratch/raw/master/dataset/train-images-idx3-ubyte.gz)
* [train-labels-idx1-ubyte.gz](https://github.com/WegraLee/deep-learning-from-scratch/raw/master/dataset/train-labels-idx1-ubyte.gz)

---

## 시리즈 소개

<a href="https://github.com/WegraLee/deep-learning-from-scratch-3/blob/master/%EB%B0%91%EB%B0%94%EB%8B%A5%20%EC%8B%9C%EB%A6%AC%EC%A6%88%20%EC%86%8C%EA%B0%9C.pdf"><img src="https://github.com/WegraLee/deep-learning-from-scratch-3/blob/master/%EB%B0%91%EB%B0%94%EB%8B%A5%20%EC%8B%9C%EB%A6%AC%EC%A6%88%20%EC%86%8C%EA%B0%9C.png" width=1000></a>

* [『밑바닥부터 시작하는 딥러닝 ❷』 깃허브 저장소](https://github.com/WegraLee/deep-learning-from-scratch-2)
* [『밑바닥부터 시작하는 딥러닝 ❸』 깃허브 저장소](https://github.com/WegraLee/deep-learning-from-scratch-3)

## 선수지식

다음은 역자가 추천하는 선수지식입니다.
<img src="https://github.com/WegraLee/deep-learning-from-scratch-3/blob/master/%EB%B0%91%EB%B0%94%EB%8B%A5%20%EC%84%A0%EC%88%98%EC%A7%80%EC%8B%9D.png" width=1000>

---

## 새소식
:white_check_mark: **2020.02.03** - 1.6.3절의 예시 이미지를 교체했습니다. 기존 이미지는 외설성 논란이 있어 왔고, 최근 이 이미지 사용을 중지하자는 움직임이 본격화되었습니다([Nautre Nanotech](https://www.nature.com/articles/s41565-018-0337-2), [Losing Lena](https://www.losinglena.com/)). 저와 출판사도 이 취지에 공감하여 이미지를 교체하기로 했습니다. 종이책에는 12쇄부터 반영됐습니다.

:white_check_mark: **2017.04.03** - 책 본문의 수식과 그림 파일들을 모아 공유합니다. 스터디 자료 등을 만드실 때 필요하면 활용하세요.

* [equations_and_figures.zip](https://github.com/WegraLee/deep-learning-from-scratch/blob/master/equations_and_figures.zip?raw=true)

:white_check_mark: **2017.02.26** - 각 챕터 디렉터리에 README.md 파일을 추가했습니다. 각 파일의 '용도', '관련 절', '등장 페이지'를 명기했고, 책에서 각 장의 '도입부', '목차', '이번 장에서 배운 내용'을 발췌해서 책이 없어도 큰 그림을 파악할 수 있도록 했습니다.

차차 파일 안의 소스 코드에도 친절한 설명을 덧붙이도록 하겠습니다.

:white_check_mark: **2017.02.20** - 3쇄가 출간되었습니다. 크고 작은 오류를 잡는 김에 책 전체를 한 번 더 교정했습니다. 그렇다고 다른 책이 된 게 아니니 1, 2쇄를 보신 분은 오탈자 정보만 확인하시면 충분합니다. 살아 있는 책으로 만들기 위해 이번처럼 기회가 올 때마다 지속해서 품질을 업그레이드할 것이니 궁금하거나 설명이 잘 이해되지 않으면 언제든 문의하세요~

## 책 미리보기
[issuu](https://issuu.com/hanbit.co.kr/docs/____________________________________38d0e6451f0ddf) | [SlideShare](http://www.slideshare.net/wegra/ss-70456623) | [Yumpu](https://www.yumpu.com/xx/document/view/56594155/-)

## 파일 구성

|폴더 이름 |설명                         |
|:--        |:--                          |
|ch01       |1장에서 사용하는 소스 코드 |
|ch02       |2장에서 사용하는 소스 코드    |
|...        |...                          |
|ch08       |8장에서 사용하는 소스 코드    |
|common     |공통으로 사용하는 소스 코드  |
|dataset    |데이터셋용 소스 코드 |


소스 코드 해설은 책을 참고하세요.

## 요구사항
소스 코드를 실행하려면 아래의 소프트웨어가 설치되어 있어야 합니다.

* 파이썬 3.x
* NumPy
* Matplotlib

※ Python은 3 버전을 이용합니다.

## 실행 방법

각 장의 디렉터리로 이동한 후 파이썬 명령을 실행하세요(**다른 디렉터리에서는 제대로 실행되지 않을 수 있습니다!**).

```
$ cd ch01
$ python man.py

$ cd ../ch05
$ python train_nueralnet.py
```

## 라이선스

이 저장소의 소스 코드는 [MIT 라이선스](http://www.opensource.org/licenses/MIT)를 따릅니다.
비상용뿐 아니라 상용으로도 자유롭게 이용하실 수 있습니다.

## 책의 오류

이 책의 오탈자 등 오류 정보는 아래 페이지에서 확인하실 수 있습니다.

http://www.hanbit.co.kr/store/books/look.php?p_code=B8475831198


## 머신러닝/딥러닝 번역 용어표

이 책을 번역하며 정리한 [용어표](https://docs.google.com/spreadsheets/d/1ccwGiC01X-gs3PPcXPUz67W9rS6l994LD4AL18KF1_0)입니다.
