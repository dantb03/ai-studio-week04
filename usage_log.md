# AI 오케스트레이션 스튜디오 4주차
## AI 활용 기록
1. buggy_1.py 미사용<tr>
2. buggy_2.py 미사용<tr>
3. buggy_3.py 미사용<tr>
4. buggy_4.py<tr>
### 프롬프트 전문
```text
df["revenue"] = df["price"] * df["quantity"]
total = df["revenue"].sum()
 avg_price = df["price"].mean()
이 코드는 CSV 매출 데이터를 읽어 각 카테고리별 가격과 수량을 계산하여 매출액과 가격의 평균을 구하는 코드야. 문제는 print(df.isna().sum()) 실행결과 price의 항목에 결측치가 2개 존재해. 그리고 print(df["price"].describe())와 print(df["quantity"].describe()) 실행 결과 음수값과 비정상적으로 큰 값이 존재해. 이걸 해결하는 방법은 결측치의 경우 0으로 바꾸거나 결측치가 있는 항목을 없애는거야. 비정상적인 값도 마찬가지로 항목을 없엘수도 있고 적당한 수를 집어넣을수 있어. 참고로 음수값같은 경우에는 그 항목에 정해진 값이 존재해서 그걸로 바꾸는것도 방법이야. 어떤 방법을 채택하는게 좋을지 이유와 함께 제안해줘. 코드를 수정하는건 내가 방법이 합당한지 판단하고 할게. 
```
### 답변
결측치와 비정상적으로 큰 값들은 항목을 아예 제거하고 음수값은 정해진 값으로 변경하는것을 추천하였다.<tr>
의견이 일치하여서 답변을 채택하고 수정하여 검증한 결과 총 매출액은 151,198,388,824원에서 439,272,600원 평균 단가는 28,342원에서 8,280원으로 정상화 되었다.
5. buggy_5.py<tr>
### 프롬프트 전문
```text
for i in range(len(prices)):
        diff = prices[i + 1] - prices[i]      # <-- 여기가 문제의 줄
        if abs(diff) >= threshold:
            jumps.append((i, prices[i], prices[i + 1], diff))

이 코드는 prices라는 리스트의 값들에 갑자기 비정상적인 크기의 변화가 생기면 감지하고 jumps에 저장하는 코드야. 근데 문제의 줄에서 오류가 이렇게 나

Traceback (most recent call last):
  File "c:\AI_Assignments\ai-studio-week04\buggy_5.py", line 47, in <module>
    jumps = find_big_jumps(prices)
  File "c:\AI_Assignments\ai-studio-week04\buggy_5.py", line 40, in find_big_jumps
    diff = prices[i + 1] - prices[i]      # <-- 여기가 문제의 줄
           ~~~~~~^^^^^^^

IndexError: list index out of range.

이 오류가 생기는 원인을 설명해줘. 내 생각은 i가 prices의 마지막 인덱스인데 i+1값을 호출해서 오류가 나는 것 같아. 내 생각이 맞는지 확인해줘 그리고 원인 검증용 코드를 먼저 제안해줘. 코드 수정은 그 다음에 할게 
```
### 답변
가설이 맞다고 대답후 부가적인 설명을 덧붙여 검증코드 제안을 채택하였다. 검증 결과 len(prices)-1까지 코드가 돌고 i에서 오류가 나는 것을 확인였다.<tr>
따라서 for문에 루프를 len(prices)-1까지만 돌게 하는 수정을 한 후 AI에 의견을 물어봤다.

```text
r i in range(len(prices) - 1):
으로 고쳤더니 에러가 더이상 나지 않아. 에러가 나지 않는 이유를 설명해주고 이 해결이 적합한지 판단해줘
```
AI의 설명은 i가 len(prices) - 1 와 i+1을 비교하며 리스트의 정상적인 마지막 인덱스까지만 호출된다는 설명을 하였고 본인은 그 설명이 적절하다고 판단했다.