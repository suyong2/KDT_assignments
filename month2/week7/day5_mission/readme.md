- 데이터 전처리와 속성 생성에 대한 간단한 설명
=> actual_delivery_time 컬럼과 created_at컬럼을 datetime64[ns] 로 타입 변경.
=> 위 두 컬럼의 차로 taken_time 컬럼생성.
=> taken_time 컬럼을 초단위로 바꿔 int64형으로 변경
=> 결측값 가진 행은 삭제
=> store_primary_category 범주형 컬럼은 숫자형으로 매핑해 변경.
=> taken_time컬럼 분리와, actual_delivery_time컬럼 제거.
=> created_at 컬럼 숫자(int64)로 변경.


- 학습을 위해서 어떤 모델을 사용했는지 그리고 어떠한 손실함수를 사용했는지를 간단히 설명
=> 모델: sklearn.linear_model.LinearRegression 
=> 손실함수: LinearRegression 자체 손실함수(residual sum of squares)

- 테스트 데이터에 대한 평가지표들
=> RMSE: 1045.1158985838679
=> Under-prediction의 비율: 0.41637273865058594
