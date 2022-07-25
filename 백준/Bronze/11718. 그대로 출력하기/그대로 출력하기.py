while True:
    try:
        print(input())
    except EOFError:  # 파일의 끝이면 break (없으면 무한 루프)
        break
        
# EOF(End of File; 파일의 끝)