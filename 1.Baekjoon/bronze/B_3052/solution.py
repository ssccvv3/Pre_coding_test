# 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다.
# 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.

temp = []

for _ in range(10) :
    a = int(input())
    temp.append(a%42)

result = set(list(temp))

print(len(result))