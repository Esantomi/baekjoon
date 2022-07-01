while True:
    try:
        A, B = map(int, input().split())
        print(A + B)
    except:
        break  # 인수(argument)로 int가 아닌 값이 들어왔을 때 루프 종료