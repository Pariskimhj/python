#!/usr/bin/env python
# coding: utf-8

# In[20]:


# 서랍의 비밀번호가 생각이 나지 않는다.
# 비밀번호 P는 000부터 999까지 번호 중의 하나이다.
# 주어지는 번호 K부터 1씩 증가하며 비밀번호를 확인해 볼 생각이다.
# 예를 들어 비밀번호 P가 123 이고 주어지는 번호 K가 100 일 때, 100부터 123까지 24번 확인하여 비밀번호를 맞출 수 있다.
# P와 K가 주어지면 K부터 시작하여 몇 번 만에 P를 맞출 수 있는지 알아보자.

# [입력]

# 입력으로 P와 K가 빈 칸을 사이로 주어진다.

# [출력]

# 몇 번 만에 비밀번호를 맞출 수 있는지 출력한다.
 
# [시나리오]
# 1. 비밀번호 P와 주어지는 번호 K 숫자 2개를 입력 받는다 input
# 2. 숫자를 나눈 리스트 만들기 split()
# 3. K - P +1

num = list(map(int, input().split()))
print(num[0] - num[1] + 1)

