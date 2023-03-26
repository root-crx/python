times = 5 #这是机会的次数，可以改。

while times > 0:
    a = input('What is your number? ')
    b = int(a)

    if b == 8: #'8'是你想让别人猜的数字，可以改。
        print('''Congratulations! 
You are right!
Well done!''')
        break
    else:
        if b < 8: #这是和第二个注释相配套的数字，第二个是多少，也要把它给改了。
            print('Thinking of larger numbers of this......')
        else:
            print('Thinking of smaller numbers of this......')
    times = times - 1
    print('你还有' + (str(times)) + '机会，请珍惜你的机会。')

print(''
      '')

print('Game over.')
# 这是一个小游戏，让别人猜你心里想的数的……
# 如果直接运行，那么：一共有5次机会，数字是'8'，系统还会给你提示，说是大了还是小了。


# 这个吧，也是有些无聊
