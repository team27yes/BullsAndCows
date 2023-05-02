import random
def get_num():
    return random.sample(range(0, 10), 4)

A = get_num()

num = []
while A != num:
    num = list(map(int, input("숫자 0부터 9까지 네개 입력하세요: ").split()))
    if (len(num) != 4) or (len(set(num)) != 4) : 
        print("올바른 값을 입력하세요")
        continue
    bulls = 0
    cows = 0
    for i in range (len(A)):
        if num[i] == A[i]:
            bulls += 1
            cows -= 1
    cows_result = set(num) & set(A)
    cows += len(cows_result)
    print(f"Bulls : {bulls}, cows : {cows}")

print("정답")