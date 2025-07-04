# 1단계: 변수 선언
num = 0
players =["playerA", "playerB"]
turn = 0
# 2단계: input() 값으로 정수입력받기

# 3단계: if문을 사용하여 올바른지 확인
while True:
    print(f"\n{players[turn]}의 차례입니다.")

    while True:
        a = int(input("정수를 입력하세요: "))
        if a <= 0:
                print("정수를 입력해주세요.")
                continue
        if a not in [1, 2, 3]:
                print("1, 2, 3 중 하나를 입력해주세요.")
                continue
        break

    #4단계: 입력받은 값
    for _ in range(a):
        num += 1
        print(f"{players[turn]}: {num}")
        if num >= 31:
            print(f"{players[turn-1]} win!")
            exit()
    turn = (num - 1) % 2
    
    # 5단계: 입력받은 값

