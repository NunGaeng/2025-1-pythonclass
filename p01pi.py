# 오일러공식을 이용한 파이 근사값 구하기
n = 1
result = 1

# while문
while n <= 10000:
    a = ((2 * n + 1) ** 2 - 1) / ((2 * n + 1) ** 2)
    result = result * a
    n = n + 1
print(result*4)

pilist = [

]

# for문
n = 1
p = 1
for n in range(1, 100000):
    p = p * ((2 * n + 1) ** 2 - 1) / ((2 * n + 1) ** 2)
    #print(p*4, ',')
    pilist.append(p*4)



import matplotlib.pyplot as plt
plt.plot(pilist)
plt.show()
