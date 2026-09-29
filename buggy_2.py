# -*- coding: utf-8 -*-
"""
buggy_2.py  ―  카테고리별 매출 집계 (pandas 버전)

dirty_sales.csv를 pandas로 읽어 카테고리별 매출 합계를 구하려 한다.
그런데 실행하자마자 죽는다.

[과제] Traceback을 얻어 예외 타입을 확인하고,
       '원인을 데이터에서 직접 확인'한 뒤(힌트: 실제 컬럼명이 무엇인가?)
       코드를 수정하라.

[진단보고] KeyError: '단가'
  File "c:\AI_Assignments\ai-studio-week04\buggy_2.py", line 20, in summarize
    df["매출액"] = df["단가"] * df["수량"]        # <-- 여기가 문제의 줄
                   ~~^^^^^^^^
파일을 df로 읽어왔을때 "단가"라는 칼럼이 존재하지 않아 에러가 났다.
print(df.columns)로 df의 칼럼명을 확인해보니 전부 영어로 되어있었고 수량도 존재하지 않아 마찬가지로 오류를 불러일으킬것으로 예상된다.
따라서 각각 "price"와 "quantity"로 수정하면 에러가 해결될 것이다.
"""
import pandas as pd

def load(path):
    df = pd.read_csv(path, encoding="utf-8")
    return df

def summarize(df):
    # 단가 x 수량으로 매출액 컬럼을 만든 뒤 카테고리별 합계를 낸다
    print(df.columns)
    #df["매출액"] = df["단가"] * df["수량"]        # <-- 여기가 문제의 줄
    df["매출액"] = df["price"] * df["quantity"]  # FIXED: 컬럼명을 영어로 수정
    return df.groupby("category")["매출액"].sum()

if __name__ == "__main__":
    df = load("dirty_sales.csv")
    result = summarize(df)
    print(result)
