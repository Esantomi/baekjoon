import math

def vac_asgmt(vac_num: int, ko_page: int, math_page: int, ko_per_day: int, math_per_day: int) -> int:
    
    ko_day = math.ceil(ko_page / ko_per_day)        # 국어 숙제 소요 일수
    math_day = math.ceil(math_page / math_per_day)  # 수학 숙제 소요 일수
    
    return vac_num - max(ko_day, math_day)  # 하루에 국어, 수학 중 한 과목이 아닌 두 과목 모두 풀 수 있으므로 큰 값 빼기

if __name__ == "__main__":  # __name__은 모듈 이름 저장, 인터프리터로 직접 실행 시 모듈 이름 대신 "__main__" 저장
    
    L = int(input())  # 방학 일수
    A = int(input())  # 국어 총쪽수
    B = int(input())  # 수학 총쪽수
    C = int(input())  # 국어 일일 최대 쪽수
    D = int(input())  # 수학 일일 최대 쪽수
    
    print(vac_asgmt(L, A, B, C, D))
    

# 간단한 버전
# import math

# L = int(input())
# A = int(input())
# B = int(input())
# C = int(input())
# D = int(input())

# print(L - max(math.ceil(A/C), math.ceil(B/D)))