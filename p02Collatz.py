# 2025.4.2 파이썬수업 프로젝트 두번째
# 콜라츠 추측, 또는 우박수
# 1부터 1000까지 숫자 중, 가장 많은 단계를 거쳐서 1로 가는 수는 무엇인가?, 가장 많은 단계는 몇 단계인가
# 규칙: n이 짝수 -> n/2
#      n이 홀수 -> 3 * n + 1
# 예: 5 -> 16 -> 8 -> 4 -> 2 -> 1  (5단계)

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
max_sum = 0
max_number = 0
for a in range(1, 100):
    n = a
    sum = 0

    print(f"시작 숫자 : {n}")

    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1

        sum = sum + 1
        print(n)

    print(f"{a} : {sum}단계\n")
    if sum > max_sum:
        max_sum = sum
        max_number = a

print(f"가장 많은 단계를 거친 숫자 : {max_number}")
print(f"{max_number}의 단계 : {max_sum}")

# n = 99
#
# while n != 1:
#     if n % 2 == 1:
#         n = 3 * n + 1
#     else:
#         n = n / 2
#     print(n)