import itertools as its
words = "1234567890"
r = its.product(words,repeat=6)
dic = open("pass.txt","a")
for i in r:
    dic.write("".join(i))
    dic.write("".join("\n"))
dic.close()

# 6位数字密码字典python脚本生成
# ！！！请不要用于非法用途，后果与作者无关！！！
