# 2025.3.19
# 파이썬 수업, 조건문

grade = "아직 모름"
score = int(input("점수를 입력하세요 : "))
if score > 60:
    grade = "합격"
else:
    if score > 50:
        grade = "임시합격"
    else:
        grade = "불합격"

print(grade)

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
else:
    grade = 'F'

print(grade)