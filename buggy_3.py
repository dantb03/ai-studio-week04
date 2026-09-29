# -*- coding: utf-8 -*-
"""
buggy_3.py  ―  데이터 로드 후 카테고리별 집계

load_and_clean()으로 데이터를 읽어 정제한 뒤,
그 결과를 groupby로 집계하려 한다.
그런데 집계 단계에서 이상한 에러가 난다.

[과제] Traceback의 예외 타입을 확인하고,
       'NoneType ...' 메시지가 가리키는 '이 변수를 만든 직전 단계'를
       역추적하여 원인 함수를 찾아 수정하라.

[진단보고] AttributeError: 'NoneType' object has no attribute 'groupby'
File "c:\AI_Assignments\ai-studio-week04\buggy_3.py", line 28, in main
    result = df.groupby("category")["revenue"].sum()   # <-- 여기서 죽는다
             ^^^^^^^^^^
df이 dataframe이었으면 groupby() 메서드가 작동됬겠지만 'NoneType'이어서 에러가 발생한 것으로 보인다.
print(type(df)) 실행결과 df가 'NoneType'인것으로 보아 df가 아무런 값도 반환 받지 못했음을 알 수 있다.
윗줄에 df = load_and_clean 메서드로 거슬러 올라가면 return 값이 보이지 않는다.
return df를 추가하면 코드가 정상적으로 작동할 것이다.
"""
import pandas as pd

def load_and_clean(path):
    df = pd.read_csv(path, encoding="utf-8")
    # price 컬럼을 숫자로 정제
    df["price"] = (df["price"].astype(str)
                              .str.replace(",", "")
                              .str.replace("원", "")
                              .str.strip())
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df["revenue"] = df["price"] * df["quantity"]
    # (여기서 정제된 df를 돌려주려고 했는데...)   <-- 무언가 빠져 있다
    return df

def main():
    df = load_and_clean("dirty_sales.csv")
    print(type(df))
    result = df.groupby("category")["revenue"].sum()   # <-- 여기서 죽는다
    print(result)

if __name__ == "__main__":
    main()
