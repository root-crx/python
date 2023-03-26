import random
import string

n = "0123456789"
s = string.ascii_letters
i = 0
psd = ""

ku = n+s

while True:
    while i<6:
        temp = random.choice(ku)
        psd += temp
        i += 1
    for o in n:
        if o not in psd:
            a = True
        else:
            a = False
            print(psd)
            break
    if psd.isdigit() or a:
        i = 0
        psd = ""
        continue
    else:
        break


# 求6位随机密码（数字 + 字母）
# 这个比较有用
