import random
def get_num():
    return random.sample(range(0, 10), 4)

A = get_num()
num = list(map(int, input("숫자 0부터 9까지 네개 입력하세요: ").split()))
print(num)
#1
