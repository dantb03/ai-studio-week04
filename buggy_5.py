# -*- coding: utf-8 -*-
"""
buggy_5.py  ―  '앞 행 대비 가격 변화'가 큰 행 찾기

정제한 price를 앞뒤로 비교하며 급변 지점을 찾으려 한다.
데이터에는 이상치(-4500, 9999999)도 섞여 있어 변화폭이 튀는 구간이 있다.
그런데 반복문이 끝까지 가지 못하고 죽는다.

[과제] Traceback으로 예외 타입을 확인하라(힌트: 반복문 경계).
       print 디버깅이 500줄 출력을 뒤져야 한다면,
       디버거의 '조건부 중단점'(예: 조건식  i >= len(prices) - 2)을 걸어
       문제의 반복 지점에서 곧바로 멈춰 원인을 관찰한 뒤 수정하라.

[진단보고] IndexError: list index out of range
File "c:\AI_Assignments\ai-studio-week04\buggy_5.py", line 29, in find_big_jumps
    diff = prices[i + 1] - prices[i]      # <-- 여기가 문제의 줄
           ~~~~~~^^^^^^^
prices의 인덱스를 벗어나는 오류가 나는 것을 보아 prices[i+1]에서 i가 prices의 마지막 인덱스이고 그 다음을 호출하여 오류가 난것으로 예상된다.
이 코드는 비정상적인 값을 찾기위해 prices의 양옆 값들을 비교하기 때문에 마지막 항목은 다음값이 없으므로 비교할 필요가 없다.
i >= len(prices) - 1 실행결과 값이 한번 출력되고 오류가 나는것으로 보아 i-1까지만 반복문이 돌면 오류가 나지 않을 것이다.
"""
import pandas as pd

def load_prices(path):
    df = pd.read_csv(path, encoding="utf-8")
    df["price"] = (df["price"].astype(str)
                              .str.replace(",", "")
                              .str.replace("원", "")
                              .str.strip())
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    # 결측은 0으로 두고, 리스트로 변환해 순회한다
    return df["price"].fillna(0).tolist()

def find_big_jumps(prices, threshold=100000):
    jumps = []
    for i in range(len(prices) - 1): # FIXED: 마지막 항목은 비교할 필요가 없으므로 -1
        ''' 디버깅용
        if i >= len(prices) - 1:
            print("오류가 나기 직전 위치")
        else:
            print("오류 안남")
        '''
        diff = prices[i + 1] - prices[i]      # <-- 여기가 문제의 줄
        if abs(diff) >= threshold:
            jumps.append((i, prices[i], prices[i + 1], diff))
    return jumps

if __name__ == "__main__":
    prices = load_prices("dirty_sales.csv")
    jumps = find_big_jumps(prices)
    print(f"급변 지점 {len(jumps)}건")
    for row in jumps[:10]:
        print(row)
