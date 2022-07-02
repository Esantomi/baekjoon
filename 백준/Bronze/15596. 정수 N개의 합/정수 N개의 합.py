def solve(a: list) -> int:
    ans = 0
    for i in a:
        ans += i
    return ans

## 다른 방법
# def solve(a: list) -> int:
#     return sum(a)