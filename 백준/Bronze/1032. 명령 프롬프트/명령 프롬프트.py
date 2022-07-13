N = int(input())

file_name = list(input())  # 비교를 위한 파일명
file_name_len = len(file_name)

for _ in range(N-1):
  next_file = list(input())
  for i in range(file_name_len):
    if file_name[i] != next_file[i]:
      file_name[i] = '?'

print(''.join(file_name))  # '구분자'.join(리스트)