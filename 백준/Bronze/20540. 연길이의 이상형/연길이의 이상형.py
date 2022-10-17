id_pairs = {'E':'I', 'I':'E', 'N':'S', 'S':'N',
            'T':'F', 'F':'T', 'J':'P', 'P':'J'}
mbti = "".join([id_pairs[i] for i in input()])

print(mbti)