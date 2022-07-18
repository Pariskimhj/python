#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 문제 출처 : 프로그래머스

# [문제 설명]

# 자연수 n이 매개변수로 주어집니다. n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 return 하도록 solution 함수를 완성해주세요. 답이 항상 존재함은 증명될 수 있습니다.

# [제한사항]
# 3 ≤ n ≤ 1,000,000

# [입출력 예]

# n	result
# 10	3
# 12	11

# [입출력 예 설명]

# 입출력 예 #1

# 10을 3으로 나눈 나머지가 1이고, 3보다 작은 자연수 중에서 문제의 조건을 만족하는 수가 없으므로, 3을 return 해야 합니다.

# 입출력 예 #2

# 12를 11로 나눈 나머지가 1이고, 11보다 작은 자연수 중에서 문제의 조건을 만족하는 수가 없으므로, 11을 return 해야 합니다.

def solution(n):          # 함수 정의
    for i in range(2, n): # 2부터 n-1까지 숫자 확인 / 1과 n은 n으로 나눌 때 항상 나머지가 0이기 때문에 제외 
        if n % i == 1:    # n을 2부터 n-1까지의 숫자로 나눈 결과가 1일 때
            answer = i    # answer은 i
            break         # 나머지가 1이 되도록 하는 가장 작은 자연수가 나오면 반복문 탈출
    return answer         # 결과 출력
