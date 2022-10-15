votes = [input() for _ in range(9)]

print('Lion' if votes.count('Lion') > votes.count('Tiger') else 'Tiger')