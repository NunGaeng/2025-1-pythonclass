# 2025.4.2 파이썬수업 프로젝트 두번째
# 콜라츠 추측, 또는 우박수
# 1부터 1000까지 숫자 중, 가장 많은 단계를 거쳐서 1로 가는 수는 무엇인가?, 가장 많은 단계는 몇 단계인가
# 규칙: n이 짝수 -> n/2
#      n이 홀수 -> 3 * n + 1
# 예: 5 -> 16 -> 8 -> 4 -> 2 -> 1  (5단계)
import numpy as np
import statistics
import time

from mkl import second

#from p02Collatz import maxvalue
from p02Collatzfunc import collatz

MAXNUM = 100

# 2025.4.9 우박수 프로젝트 두번째: 기본 통계량 구하기
# numpy 배열, list 두가지 방식으로 시험
# 구하는 통계량 : 평균, 중앙값, 표준편차


# 리스트
start = time.time()

ncountl = []
maxvalue = 0
maxvaluen = 0
second_value = 0
third_value = 0

for n in range(1,MAXNUM):
    ncount = collatz(n)
    ncountl.append(ncount)

for n_count in ncountl[:]:
    if n_count > maxvalue:
        second_value = maxvalue
        maxvalue = n_count
    elif n_count > second_value:
        second_value = n_count
    elif n_count > third_value:
        third_value = n_count
nmax = ncountl.index(max(ncountl))+1
second_nmax = ncountl.index(second_value)+1
third_nmax = ncountl.index(third_value)+1

# 최대값, 평균, 중앙값, 표준편차, 최빈값
print(f'최대값 = {max(ncountl)}')
print(f'해당숫자 {nmax}')
print(f'2번째 값 {second_nmax}')
print(f'3번째 값 {third_nmax}')
print(f'평균 = {statistics.mean(ncountl):.5f}')
print(f'중앙값 = {statistics.median(ncountl):.5f}')
print(f'표준편차 = {statistics.stdev(ncountl):.5f}')
#print(f'최빈값 = {statistics.mode(ncountl):.5f}')

end = time.time()
print(f'{end - start:.5f}초가 걸렸습니다')

# numpy
start = time.time()
maxvalue = 0
second_value = 0
third_value = 0

ncounta = np.zeros(MAXNUM-1)
for n in range(1,MAXNUM):
    #print(f'{n=}')
    ncount = collatz(n)
    ncounta[n-1] = ncount

for n_count in ncounta[:]:
    if n_count > maxvalue:
        second_value = maxvalue
        maxvalue = n_count
    elif n_count > second_value:
        second_value = n_count
    elif n_count > third_value:
        third_value = n_count

nmax = np.argmax(ncounta)+1
second_nmax = np.where(ncounta == second_value)[0][0]+1
third_nmax = np.where(ncounta == third_value)[0][0]+1


# 최대값, 평균, 중앙값, 표준편차, 최빈값
print(f'최대값 = {np.max(ncounta)}')
print(f'해당숫자 {nmax}')
print(f'2번째 값 {second_nmax}')
print(f'3번째 값 {third_nmax}')
print(f'평균 = {np.mean(ncounta):.5f}')
print(f'중앙값 = {np.median(ncounta):.5f}')
print(f'표준편차 = {np.std(ncounta):.5f}')
#print(f'최빈값 = {np.bincount(ncounta):.5f}')

end = time.time()
print(f'{end - start:.5f}초가 걸렸습니다')

# 1부터 1000까지 숫자 중 적으면 단계 표시
# n = int(input('1부터 1000까지 숫자 중 적어주세요 : '))
# sum = 0
# while n != 1:
#     if n % 2 == 0:
#         n = n / 2
#         print(n)
#         sum = sum + 1
#     else:
#         n = 3 * n + 1
#         print(n)
#         sum = sum + 1
#
# print(sum,'단계')

# 1부터 99까지 반복, 가장 많이 거친 단계 표시
# max_sum = 0
# max_number = 0
# for a in range(1, 100):
#     n = a
#     sum = 0
#
#     print(f"시작 숫자 : {n}")
#
#     while n != 1:
#         if n % 2 == 0:
#             n = n / 2
#         else:
#             n = 3 * n + 1
#
#         sum = sum + 1
#         print(n)
#
#     print(f"{a} : {sum}단계\n")
#     if sum > max_sum:
#         max_sum = sum
#         max_number = a
#
# print(f"가장 많은 단계를 거친 숫자 : {max_number}")
# print(f"{max_number}의 단계 : {max_sum}")

n = 0

# maxvalue = 0
# maxvaluen = 0
# ncount = 0
# for n in range(1,100):
#     #print(f'{n=}')
#     ncount = 0
#     i = n
#
#     while i != 1:
#         if i % 2 == 1:
#             i = 3 * i + 1
#         else:
#             i = i / 2
#         ncount = ncount + 1
#
#     print(f'{ncount}')
#     if maxvalue < ncount:
#         maxvalue = ncount
#         maxvaluen = n
#
# print(f'{maxvalue=}, {maxvaluen}')

# maxvalue = 0
# maxvaluen = 0
#
# second_value = 0
# second_n = 0
#
# third_value = 0
# third_n = 0
#
# for n in range(1, 100):
#     ncount = 0
#     i = n
#
#     while i != 1:
#         if i % 2 == 1:
#             i = 3 * i + 1
#         else:
#             i = i / 2
#         ncount += 1
#
#     if ncount > maxvalue:
#         second_value = maxvalue
#         second_n = maxvaluen
#         maxvalue = ncount
#         maxvaluen = n
#     elif ncount > second_value:
#         second_value = ncount
#         second_n = n
#     elif ncount > third_value:
#         third_value = ncount
#         third_n = n
#
# print(f"n = {maxvaluen}, count = {maxvalue}")
# print(f"n = {second_n}, count = {second_value}")
# print(f"n = {third_n}, count = {third_value}")

