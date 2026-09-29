# -*- coding: utf-8 -*-
"""
buggy_1.py  ―  판매 데이터 매출 집계 (csv 모듈 버전)

dirty_sales.csv를 한 줄씩 읽어 '매출액 = 단가 x 수량'을 누적한다.
잘 돌아가는 것처럼 보이지만, 어떤 행에서 갑자기 멈춘다.

[과제] 이 스크립트를 실행해 Traceback을 얻고,
       진단 3단계 루틴(무엇이 / 어디서 / 왜)으로 원인을 특정한 뒤
       전처리로 해결하라. (힌트: 예외 타입은 무엇인가?)

[진단보고] ValueError: invalid literal for int() with base 10: '5,200'
File "c:\AI_Assignments\ai-studio-week04\buggy_1.py", line 21, in calc_total
    price = int(row["price"])        # <-- 여기가 문제의 줄
'ValueError'인 것을 보아 int() 함수가 '5,200'을 정수형으로 변환해주지 못해 에러가 발생하였다.
print(type(row["price"]))의 값이 str으로 표시되는 것을 보아 문자열이고 ,를 제거해주면 에러를 해결할 수 있을 것으로 예상된다.

[진단보고2] ValueError: invalid literal for int() with base 10: '4200원'
File "c:\AI_Assignments\ai-studio-week04\buggy_1.py", line 27, in calc_total
    price = int(row["price"])        # <-- 여기가 문제의 줄
'ValueError'인 것을 보아 int() 함수가 '4200원'을 정수형으로 변환해주지 못해 에러가 발생하였다.
이 전 에러와 같은 문제이므로 문자열에서 원을 제거해주면 에러를 해결할 수 있을 것으로 예상된다.

[진단보고3] ValueError: invalid literal for int() with base 10: ''
File "c:\AI_Assignments\ai-studio-week04\buggy_1.py", line 34, in calc_total
    price = int(row["price"])        # <-- 여기가 문제의 줄
'ValueError'인 것을 보아 int() 함수가 ''을 정수형으로 변환해주지 못해 에러가 발생하였다.
빈 문자열은 정수형으로 변환할 수 없으므로, 빈 문자열을 0으로 대체하면 에러를 해결할 수 있을 것으로 예상된다.

"""
import csv

def calc_total(path):
    total = 0
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)  # 사전타입으로 데이터를 읽음.
        for i, row in enumerate(reader):
            row["price"] = row["price"].replace(',', '')  # FIXED: 콤마 제거
            row["price"] = row["price"].replace('원', '')  # FIXED: '원' 제거
            if row["price"] == '':
                row["price"] = '0'
            print(row["price"])
            price = int(row["price"])        # <-- 여기가 문제의 줄
            qty = int(row["quantity"])
            total += price * qty
    return total

if __name__ == "__main__":
    total = calc_total("./Week4/dirty_sales.csv")
    print(f"총 매출액: {total:,}원")
