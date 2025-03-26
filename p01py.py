# 오일러공식을 이용한 파이 근사값 구하기
n = 1
result = 1

# while문
while n <= 100:
    a = ((2 * n + 1) ** 2 - 1) / ((2 * n + 1) ** 2)
    result = result * a
    n = n + 1
print(result*4)

# for문
b = 1
p = 1
for b in range(1, 100):
    p = ((2 * b + 1) ** 2 - 1) / ((2 * b + 1) ** 2)
print(p*4)


import matplotlib.pyplot as plt
plt.plot([1,3,4])
plt.show()
