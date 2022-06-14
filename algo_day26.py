#!/usr/bin/env python
# coding: utf-8

# In[19]:


# 문제 출처 : SW Expert Academy

# 연월일 순으로 구성된 8자리의 날짜가 입력으로 주어진다.
# 해당 날짜의 유효성을 판단한 후, 날짜가 유효하다면

# [그림1] 과 같이 ”YYYY/MM/DD”형식으로 출력하고,
# 날짜가 유효하지 않을 경우, -1 을 출력하는 프로그램을 작성하라.

# 연월일로 구성된 입력에서 월은 1~12 사이 값을 가져야 하며
# 일은 [표1] 과 같이, 1일 ~ 각각의 달에 해당하는 날짜까지의 값을 가질 수 있다.
# ※ 2월의 경우, 28일인 경우만 고려한다. (윤년은 고려하지 않는다.)

# [입력]

# 입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
# 다음 줄부터 각 테스트 케이스가 주어진다.

# [출력]

# 테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

for t in range(int(input())):                     # T 입력받기
    input_data = input()                          # 날짜 입력받기
    year = input_data[:4]                         # 년
    month = input_data[4:6]                       # 월
    day = input_data[6:]                          # 일
    if int(month) in [1, 3, 5, 7, 8, 10, 12]:     # 한 달에 31일인 month일 때
        if int(day) in range(1,31+1):             # day가 1~31일이면
            print(f'#{t+1} {year}/{month}/{day}') # 날짜 출력
        else:
            print(f'#{t+1} -1')                   # 날짜 범위를 벗어나면 -1 출력
    elif int(month) in [4, 6, 9, 11]:             # 한 달에 30일인 month일 때
        if int(day) in range(1,30+1):             # day가 1~30일이면
            print(f'#{t+1} {year}/{month}/{day}') # 날짜 출력
        else:
            print(f'#{t+1} -1')                   # 날짜 범위를 벗어나면 -1 출력
    elif int(month) == 2:                         # 한 달에 28일인 month일 때
        if int(day) in range(1,28+1):             # day가 1~28일이면
            print(f'#{t+1} {year}/{month}/{day}') # 날짜 출력
        else:
            print(f'#{t+1} -1')                   # 날짜 범위를 벗어나면 -1 출력
    else:
        print(f'#{t+1} -1')                       # 이외의 month는 -1 출력

