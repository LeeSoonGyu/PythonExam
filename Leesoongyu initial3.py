 # 이순규
# 1.
num = 100
if num > 100:
    print('100보다 큽니다.')
else :
    if num > 50:
        print('50보다 큽니다.')
    else :
     print('50이하입니다.')

# 2.
for i in range(2,10):
    for j in range(1,10):
        print(i*j, end=' ')
        print(' ')

# 3.
multline = """It ain't over
til it's over.
by Yogi Berra"""

sents = []
words = []

# 3-1
# for sen in multline.split("\n"):
    # sents.append(sen)
    # for word in sen.split():
        # words.append(word)
# print(sents)
# print(" ".join(sents))
# print(words)
# p = words[3][2].upper()+words[2][0:3]+words[3][2]+words[6][1]
# print(p)
lee = multline.split()
print(lee)
gyu = " ".join(lee)
print(gyu)

# 3-2
soon = gyu[16].upper()+gyu[9]+gyu[10]+gyu[11]+gyu[16]+gyu[-10]
print(soon)
