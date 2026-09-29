# -*- coding: utf-8 -*-
"""
buggy_4.py  ―  총 매출액 집계 (에러 없이 '조용히' 틀리는 스크립트)

이 스크립트는 에러 없이 잘 돌아가고, 그럴듯한 숫자를 출력한다.
하지만 그 숫자는 '틀렸다'.

[과제] 이 스크립트는 예외를 던지지 않는다. 대신
       (1) info()/describe()로 데이터 상태를 먼저 세어 보고
       (2) '무엇이 틀렸는지 어떻게 알아챘는지'를 서술한 뒤
       (3) 결측 규모를 보고하고 처리 방법을 선택·적용하여
           올바른 총매출을 산출하라.
       (힌트: 가격 결측은 몇 건인가? 음수 가격과 9999999 같은 값은 정상인가?)

[진단보고] 결측치 테스트 코드의 결과 price 칼럼에 결측지가 2개 존재하는 것을 확인했다.
또한 price 칼럼에 음수값과 9999999이라는 비정상적인 값이 price와 quantity에 각각 존재한다.
이는 매출액이 1500억이라는 비정상적인 수치가 나오는 이유로 유추할 수 있다.
따라서 결측치와 비정상적인 값들을 제거한 뒤 매출액과 가격평균을 계산하면 정상적인 값이 나올 것으로 예상된다.
"""
import pandas as pd

def main():
    df = pd.read_csv("dirty_sales.csv", encoding="utf-8")

    # price를 숫자로 바꾼다 (빈 값은 NaN이 된다 — 그런데 그 규모를 확인하지 않았다)
    df["price"] = (df["price"].astype(str)
                              .str.replace(",", "")
                              .str.replace("원", "")
                              .str.strip())
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    ''' 디버깅용 코드
    print(df["price"].isna().sum())
    print(df.shape) # (행, 열) 크기
    print(df.info()) # 컬럼별 non-null 개수와 dtype 한눈에
    print(df.isna().sum()) # 컬럼별 결측치 개수
    print(df[df["price"].isna()].head())
    print(df["price"].describe())
    print(df.sort_values("price").head(5)) # 최소값 쪽 실제 행 확인
    print(df.sort_values("price").tail(5)) # 최대값 쪽 실제 행 확인
    print(df["quantity"].describe())
    print(df.sort_values("quantity").head(5)) # 최소값 쪽 실제 행 확인
    print(df.sort_values("quantity").tail(5)) # 최대값 쪽 실제 행 확인
    '''
    df = df.dropna(subset=["price"]) # FIXED: price 결측치 제거

    max_price_limit = 100000
    max_quantity_limit = 1000
    df = df[(df['price'] <= max_price_limit) & (df['quantity'] <= max_quantity_limit)] # FIXED: price와 quantity의 비정상적인 값 제거

    df.loc[df['price'] < 0, 'price'] = 2800 # FIXED: price가 음수인 마들렌 항목의 가격을 원래 가격인 2800으로 변경

    # 매출액 = 단가 x 수량 (NaN이 섞이면 그 행의 매출액도 NaN)
    df["revenue"] = df["price"] * df["quantity"]

    # sum()은 NaN을 조용히 건너뛰고, 음수/극단값은 그대로 더한다
    total = df["revenue"].sum()
    avg_price = df["price"].mean()

    print(f"총 매출액: {total:,.0f}원")
    print(f"평균 단가: {avg_price:,.0f}원")
    # 출력은 그럴듯하지만, 이 숫자를 그대로 믿어도 될까?

if __name__ == "__main__":
    main()
