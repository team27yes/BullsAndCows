import random

def get_num():
    return random.sample(range(0, 10), 4)

A = get_num()

while True:
    num = list(map(int, input("숫자 0부터 9까지 네개 입력하세요: ").split()))
    print(num)

    if A == num:
        print("정답입니다.")
        break
    else:
        bulls = 0
        cows = 0
        for i in range(len(A)):
            if num[i] == A[i]:
                bulls = bulls + 1
            else:
                if num[i] in A:
                    cows += 1    
        print(f"Bulls : {bulls}, Cows : {cows}")
        continue
