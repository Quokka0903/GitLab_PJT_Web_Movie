# 8기 FINAL 관통 PJT

--- 

# 내 MOM에 쏘옥 드는 MOM!
![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/a20e5c25-d627-4316-8bf4-87a033ad6d04/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221124T170621Z&X-Amz-Expires=86400&X-Amz-Signature=9c4d73918dd1f29460d7e1332c1673b0dba0b3afdd107aca49a37df27af3e60f&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject)

> 알고리즘을 사용한 영화 정보 기반 추천 서비스 (MOM)

## 

## 1. 팀원 소개

![남다른 뀨한나 프로필-001.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/2c2610d9-046d-4d29-ba46-4fa5402e331e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221124T170919Z&X-Amz-Expires=86400&X-Amz-Signature=3ca95a65c3e3dfc3523952cd5c2b9b49aca5cf5aa4bb8576acdb17985948e758&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject)

## 

## 2.  사용한 기술

![사용한 기술.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/92139574-50e3-4cc8-b438-c3f967436be5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221124T170950Z&X-Amz-Expires=86400&X-Amz-Signature=3f706af79bddb0e541306aab97055717c9b7292a68c49690bc956ce9ad3d839e&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject)

- Vue.js (Front-end)

- Django rest framework (Back-end) 

## 

## 3. 서비스 기능

![기능 구현 표.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/4ef020a3-94f0-433e-ab86-c7aa40e1e4f9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221124T171851Z&X-Amz-Expires=86400&X-Amz-Signature=3a5077c917a3eeb1d75e46bffb1a4f6c5f71692623e78ee0b3726ba4bc25b9a9&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject)

- 1019개 영화데이터 저장

## 

## 4. 프로젝트 구조

### ERD

![남다른뀨한나_ERD.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/99a5a35f-3f22-4c18-95dd-aa494ed6f363/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221124T171915Z&X-Amz-Expires=86400&X-Amz-Signature=b5bef64e2685cb2c610585f4a54567d6b3740b2704b9e9bdaf483b994671729b&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject)

### Front components

![남다른뀨한나_Templates.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/5ee6ed15-f280-4a89-8118-ce37e830c1da/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221124T171931Z&X-Amz-Expires=86400&X-Amz-Signature=7e0e60a66cc4876942dee4556e31624ed4ebe140b50ec9b39666c80461d21e35&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject)

## 5. Overview

### 도입페이지

> - 도입부페이지를 두어 컨셉을 확고히 하고 사용자가 한 눈에 앱의 정체성을 경험할 수 있도록 했습니다.
> 
> - 약 4초간 진행되며 이후 로그인 페이지로 자동으로 넘어갑니다. 

![도입부.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/e02f0753-342b-4174-9663-f0364046999a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221124T171945Z&X-Amz-Expires=86400&X-Amz-Signature=f30369966f72bdc82fa6e3edce260b4b456f5fbf99949b0be8f40c38d8b06265&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject)

### 

### 로그인 및 회원가입 페이지

> - ID와 PW 부분을 클릭하면 input태그에 커서가 자동으로 올라갑니다.
> 
> - 버튼 구현을 통해 사용자의 접근성을 용이하게 했습니다.
> 
> - 회원가입 페이지에선 반응형 input태그를 구현해 아이디는 1자리 이상, 비밀번호 8자리 이상 입력될때 문구가 자동으로 사라지며 비밀번호 재확인이 불일치하면 문구 및 경고문이 뜹니다.

![로그인 및 회원가입.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/ae8a397e-8bc2-43dc-8d7f-583bb01b58ec/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221124T171958Z&X-Amz-Expires=86400&X-Amz-Signature=88c095297196185e2a8d5f68f58ea72b4b7e6af205104ea2a3ecc722cee3df60&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject)

### 

### 회원가입 후 평점 선택 페이지

> - 첫 회원가입 후 자동으로 연결되는 페이지입니다.
> 
> - 이 페이지는 알고리즘 db저장을 위한 목적으로 생성한 페이지입니다.
> 
> - 각 장르별로 4개씩 영화가 도출되며, 3개 이상 평점을 선택하고 버튼을 눌러야 메인페이지로 이동합니다. 그렇지 않으면 경고문이 나타납니다. 

![회원가입 후 영화평점 체크 페이지.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/4d0f41bb-4aec-4890-a78c-495f9345f482/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221124T171813Z&X-Amz-Expires=86400&X-Amz-Signature=20f1e7579367a1d690eee91a185cb8431e85697bc457d02df2ecc70fef71a60f&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject)

### 

### 메인페이지 - 메인

> - 위 화면에서 평점을 다 선택했거나, 로그인을 했을 때 나타나는 화면입니다.
> 
> - 메인에는 가장 위에 알고리즘을 기반(평점과 리뷰 등의 로직 구현)으로 한 4편의 영화가 새로고침할때마다 바뀌어 등장합니다.
> 
> - 2번째 단락인 장르는 랜덤으로 해당 장르의 이름과 4개의 영화가 등장합니다.
> 
> - 알고리즘과 장르 영화는 카드 클릭 시 디테일페이지로 이동합니다. 
> 
> - 3번째 단락인 top rated movies는 tmdb를 기반으로 한 4편의 영화가 등장하며,  카드 클릭 시 tmdb의 해당영화 페이지가 등장합니다.

![메인페이지-메인.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/b48e9ac8-3a82-401d-89de-10c264d85028/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221124T171758Z&X-Amz-Expires=86400&X-Amz-Signature=295b7e1ecff9d42624f0e70fae1586d36d2df20c39061e8c96ef5a72c00daad5&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject)

### 

### 메인페이지 - 영화검색

> - 메인페이지 Navbar의 2번인 영화검색 페이지입니다. 
> 
> - 반응형으로 구현했으며, 글자를 입력할 때마다 입력한 글자, 해당 글자가 적용된 영화의 수와 영화카드가 아래 실시간으로 나타납니다.

![메인페이지-검색.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/c321a3eb-6ce7-42ce-bf26-1c19eda89473/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221124T171726Z&X-Amz-Expires=86400&X-Amz-Signature=2f95140d04a69b85e6c4d88b06154d69ffcb2cf661c33ccb1c7f89190ce2f326&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject)

### 

### 메인페이지 -영화관 찾기

> - 메인페이지 Navbar의 3번인 영화관 찾기입니다.
> 
> - 영화관 찾기 버튼 클릭 시 내위치와 모든 영화관 리스트를 도출합니다.

![영화관 찾기.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/82730643-d977-4ec3-a572-f603f5e3f4ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221124T171654Z&X-Amz-Expires=86400&X-Amz-Signature=c0b09734bc61c83d9981492b1b4fd098406737c170cecf1dae5a748c70014b4a&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject)

### 

### 메인페이지 - 나의 프로필

> - 메인페이지 Navbar의 4번인 프로필입니다.
> 
> - 이 중 후에 기술되지 않은 로그아웃과 회원탈퇴는 클릭 즉시 반영되며 로그인페이지로 이동하게 됩니다.

![메인페이지-나의프로필.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/0c922bfa-f276-40c8-813c-6d573f25bb5d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221124T171616Z&X-Amz-Expires=86400&X-Amz-Signature=f3e06e7ab037c7402c0bbcd2a12d2fcd4ecfe691cc27e7f3cd0b199560e3fb99&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject)

##### 평가한 영화 보기

> - 회원가입 후 평점체크 페이지와 디테일페이지에서 평점을 남기게 되면 이 곳 db에 저장되어 나타납니다.
> 
> - 해당 카드는 클릭 즉시 해당 영화의 디테일페이지로 이동합니다.

![프로필-평점.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/ba1cce1f-9952-4d0e-98a7-6ab6f797efdf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221124T171554Z&X-Amz-Expires=86400&X-Amz-Signature=40bb99f008858bff8515413b7d60512db5d7de22e93ccfff6aa2747636712e86&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject)

##### 

##### 리뷰 남긴 영화 보기

> - 디테일페이지에서 리뷰를 작성하면 이 곳에 바로 반영됩니다. 강한 상호연결성을 가져, 이 곳에서 삭제하면 디테일페이지의 리뷰에도 삭제가 되며 반대의 경우에도 마찬가지입니다.
> 
> - 이 곳에서도 리뷰의 수정과 삭제가 가능하며 모달을 통해 구현했고 즉시 반영됩니다.

![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/0a113899-33e5-4658-934a-05ef64fa082c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221124T171528Z&X-Amz-Expires=86400&X-Amz-Signature=6e72d13d586c8c8e55ca44ac7645d5eea4ad4c939dbe34c04628e5df5a9876f8&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject)

##### 비밀번호 변경

> - 비밀번호 수정이 가능한 페이지이며 수정 후 로그인페이지로 이동합니다.

![프로필-비밀번호 변경.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/1c9df1af-b8fe-4f0f-af78-7cbeae871d72/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221124T171457Z&X-Amz-Expires=86400&X-Amz-Signature=2661606a573b4eb91e85515fdb2360b26f45a4ae4f3df8e3e88fa2889f3a8633&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject)

### 

### 디테일페이지

> - 메인페이지의 top rated를 제외하고, 마우스호버(카드의 확대 효과)가 들어가있는 모든 카드에 이동되도록 구현한 디테일페이지입니다.
> 
> - 기본적으로 평점과 리뷰를 남길 수 있으며 리뷰 모두 보기에서 다른 사용자가 남긴 리뷰에 좋아요를 누를 수 있습니다.
> 
> - 위에 설명한 좋아요를 토대로 베스트 리뷰 2개가 디테일페이지 중단에 도출됩니다.
> 
> - 리뷰 남기기는 모달을 통해 구현했습니다.
> 
> - 더보기를 통해 overview를 확대해서 전체 내용을 읽을 수 있습니다.
> 
> - ost 보기를 통해 해당 영화의 ost를 youtube를 통해 감상할 수 있습니다.
> 
> - 최하단엔 같은 장르의 다른 영화가 4개씩 랜덤으로 도출됩니다.

![디테일페이지.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/93b9a267-32d8-447c-80f4-4b4a29dc581f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221124T171429Z&X-Amz-Expires=86400&X-Amz-Signature=6e53edad2bab3f6945cfe5436bdc130d7ed7baa4d3543913f7216fa6289a555b&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject)

> - 리뷰 모두보기 버튼을 클릭하면 전환되는 페이지입니다. 
> 
> - 기본적인 수정과 삭제가 가능하며, 변경 시 내 프로필 nav의 리뷰 모두 보기에서도 확인이 가능합니다. 
> 
> - 삭제 후 디테일페이지로 돌아갈 수 있습니다.

![디테일페이지 리뷰.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/d9800a01-9710-4176-a6ee-a2b47c3e3d39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221124T171414Z&X-Amz-Expires=86400&X-Amz-Signature=c27cc81bd352432e615f02beab6cd2f35d8d8441197d6a5f7caee0a65ca86b4f&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject)

## 6. 설치 방법

```python
Backend
$ cd final-pjt-back
$ python -m venv venv
$ source venv/Scripts/activate
$ python install -r requirements.txt
$ python manage.py migrate
$ python manage.py loaddata movies.json
$ python manage.py runserver
```

```python
Frontend
$ cd final-pjt-front
$ npm install
$ npm run serve
```

## 7. 느낀점

#### 이한나

- 프로젝트를 진행하고, 제 실력이 많이 성장했다는 것을 느낄 수 있었습니다.

- 장고 수업을 배우고 나서도, 그 구조에 대해서 잘 모르겠다는 생각이 있었습니다. 하지만 실제로 ERD를 그리고 그것에 맞추어 역참조를 하고, serializer를 만드는 과정에서 구조에 대한 이해가 되기 시작했고, 실제로 하루하루 코드가 성장한다는 것을 느낄 수 있었습니다. 하루 만에 어제 제가 쓴 코드를 더 효율적으로 짤 수 있는 방법에 대해 생각나기도 하고요!

- 확실히 front, back에 대해서 구현을 했을 때에는 뭔가 부족하다는 생각이 들었는데 css가 구성이 되고 나서는 그런 느낌이 사라진 것을 보고, css도 굉장히 중요함을 느꼈습니다

- 대략적으로 front 구조를 짜고 시작했음에도 불구하고, 프로필 구성들이 바뀜에 따라서 기존에 만들어둔 model에서 쓰지 않아도 될 것들도, 새로 만들어야할 것들도 많이 생겼습니다. 이번 경험을 통해서 시간이 걸리더라도 확실하게, ERD, 컴포넌트들을 구성하는 것이 필요함을 알 수 있었습니다!

#### 이정규

- 건강이야말로 팀에 기여할 수 있는 가장 기본적인 덕목이다.

- 빠른 소통, 남은 항목을 구조화 후 분담, 분야 구분 없이 할 수 있는 부분 먼저 수행하는 것이 프로젝트 진행 효율을 높여주었다.

- BE, FE 중 하나를 맡기보다 상황마다 필요한 부분(할 수 있는 부분)을 맡아 진행하니, 프로젝트 전반을 훑으며 지금까지 배웠던 항목들을 자연스레 되짚어보고 실행 과정을 하나하나 따라가며 효과적인 복습이 가능했다.

- 따라서 분야를 확실히 정하고 한 우물만 파는 상황이 아니라 관통프로젝트 하는 지금 시기에는 전천후 분담이 좋은 것도 같다. 마무리 단계에서 최종 프로젝트 전 페어프로젝트 연습할 때처럼 Driver와 Navigator로 나누어 진행했었는데 소통 및 복습에 유익했다.

- 사실 한나가 다 했다. 기여도 높은 사람 있으면 커피라도 사 주자 (나는 아직 안 샀다).

- CSS가 막연하게 다가왔었으나 직접 공부하면서 진행하다보니 개념이 보다 잘 정리되어 와닿는 기분이 들었다. 프로젝트 준비 기간이 길어서 더 큰 볼륨으로 준비했었더라면 좋았겠다는 아쉬움이 남았다.

- CSS도 트리 구조처럼 큰 템플릿에서부터 가지치기 식으로 부여했다면 훨씬 효율적이고 가독성 높은 코드를 짤 수 있었겠다는 아쉬움도 있었다. 그러나 개선하기에는 너무 늦은 타이밍..

- 이번에는 BE → FE → CSS 로 다 함께 옮겨가는 방식이 프로젝트 진행의 대부분을 차지했었는데, 추후 프로젝트에서는 모든 기능 및 변수 등의 명칭을 모두 정해놓은 상태에서 각자 프로그래밍하고 접합하는 방식도 도전해보고 싶다.

- 야, web fail 뜬 나도 했어.

#### 남기성

- DRF 지식에 대한 부족함을 여실히 느낌과 동시에 페어의 소중함 또한 절실히 느꼈던 일주일의 최종 PJT 기간이었습니다.

- 처음 일주일은 기획을 충분히 했음에도 불구하고, 스스로가 절차를 밟지 않고 중구난방으로 프로젝트를 준비하면서 관련 지식들 또한 머릿 속에서 차분히 정리되지 않고 흩어져 있는 느낌을 받았습니다. 지식이 기획을 따라가지 못할 때, 페어에게 질문을 계속 던지면서 해결해나가야 했지만 혼자 뭔가를 해보겠다는 마음에 시간을 많이 허비한 것 같아 아쉬웠습니다.

- 그러나 PJT 발표 주간을 맞이하면서부터 모르는 부분은 확실하게 물어보고, 해야하거나 보충해야할 부분을 계속해서 물어보고 체크하면서 PJT 진척도가 굉장히 빨라짐을 팀원 모두가 공유했고 이에 따라 매일매일 진척된 부분을 체크하면서 더욱 빨리 PJT의 완성도를 갖춰나가기 시작했습니다. 이 점은 크게 성장한 부분이라 확신합니다.

결과적으로 물론 구현하지 못한 몇 가지 기능들이 있으나, 대부분을 초기 기획한대로 수행할 수 있었고, 더러 어떤 부분은 초기 기획안보다 훨씬 완성도 있게 제작되었음을 프로그램을 돌리면서 체감했습니다. 2주 기간동안 함께 성장한 팀원들에게 너무나도 고맙고, 감사의 말씀 남깁니다.